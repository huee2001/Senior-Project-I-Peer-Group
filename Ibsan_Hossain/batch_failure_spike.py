import sqlite3

TOTAL_ROWS = 100
FAIL_AFTER_ROW = 37


def make_source_rows():
    rows = []
    for i in range(1, TOTAL_ROWS + 1):
        employee_id = f"E{i:04d}"
        full_name = f"First{i} Last{i}"
        hire_date = f"2021-01-{((i - 1) % 28) + 1:02d}"
        rows.append(
            {
                "employee_number": employee_id,
                "full_name": full_name,
                "hire_date": hire_date,
            }
        )
    return rows


def transform(row):
    parts = row["full_name"].split()

    if len(parts) != 2:
        raise ValueError("name_split_rule")

    return {
        "employee_id": row["employee_number"],
        "first_name": parts[0],
        "last_name": parts[1],
        "start_date": row["hire_date"],
    }


def insert_batch(conn, source_rows, simulate_failure=False):
    conn.execute("BEGIN")

    try:
        for row_number, source_row in enumerate(source_rows, start=1):
            transformed = transform(source_row)

            conn.execute(
                """
                INSERT INTO employees (
                    employee_id,
                    first_name,
                    last_name,
                    start_date
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    transformed["employee_id"],
                    transformed["first_name"],
                    transformed["last_name"],
                    transformed["start_date"],
                ),
            )

            if simulate_failure and row_number == FAIL_AFTER_ROW:
                raise RuntimeError(
                    f"simulated failure after writing row {FAIL_AFTER_ROW} before commit"
                )

        conn.commit()

    except Exception:
        conn.rollback()
        raise


def count_rows(conn):
    return conn.execute("SELECT COUNT(*) FROM employees").fetchone()[0]


def check_results(conn, source_rows):
    stored = conn.execute(
        """
        SELECT employee_id, first_name, last_name, start_date
        FROM employees
        ORDER BY employee_id
        """
    ).fetchall()

    stored_ids = [row[0] for row in stored]
    expected_ids = [row["employee_number"] for row in source_rows]

    missing_ids = sorted(set(expected_ids) - set(stored_ids))
    duplicate_ids = len(stored_ids) - len(set(stored_ids))

    expected_by_id = {}
    for source_row in source_rows:
        transformed = transform(source_row)
        expected_by_id[transformed["employee_id"]] = (
            transformed["first_name"],
            transformed["last_name"],
            transformed["start_date"],
        )

    incorrect_values = 0

    for employee_id, first_name, last_name, start_date in stored:
        expected = expected_by_id[employee_id]
        actual = (first_name, last_name, start_date)

        if actual != expected:
            incorrect_values += 1

    return len(missing_ids), duplicate_ids, incorrect_values


def main():
    source_rows = make_source_rows()

    conn = sqlite3.connect(":memory:", isolation_level=None)

    conn.execute(
        """
        CREATE TABLE employees (
            employee_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            start_date TEXT NOT NULL
        )
        """
    )

    # First attempt: intentionally fail after row 37 before commit.
    try:
        insert_batch(conn, source_rows, simulate_failure=True)
    except RuntimeError as error:
        print(f"Failure: {error}")

    rows_after_rollback = count_rows(conn)

    # Retry the entire batch.
    insert_batch(conn, source_rows, simulate_failure=False)

    rows_after_retry = count_rows(conn)
    missing_ids, duplicate_ids, incorrect_values = check_results(conn, source_rows)

    print(f"Rows stored after rollback: {rows_after_rollback}")
    print(f"Rows stored after retry: {rows_after_retry}")
    print(f"Missing IDs after retry: {missing_ids}")
    print(f"Duplicate IDs after retry: {duplicate_ids}")
    print(f"Rows with incorrect mapped values: {incorrect_values}")

    conn.close()


if __name__ == "__main__":
    main()
