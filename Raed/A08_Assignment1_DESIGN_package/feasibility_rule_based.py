# Feasibility test for rule-based disaster event extraction
# CSC 59866 Senior Project I - Design 3

KNOWN_EVENTS = [
    "Hurricane Sandy",
    "Hurricane Katrina",
    "Hurricane Harvey",
    "Hurricane Ian",
    "Camp Fire",
    "Northridge earthquake"
]


def extract_event(question):
    question_lower = " ".join(question.lower().split())

    for event in KNOWN_EVENTS:
        if event.lower() in question_lower:
            return event

    return None


supported_tests = [
    ("What information is available about Hurricane Sandy?", "Hurricane Sandy"),
    ("Show me reports about Hurricane Sandy.", "Hurricane Sandy"),
    ("What records exist for Hurricane Katrina?", "Hurricane Katrina"),
    ("Find information about Hurricane Katrina.", "Hurricane Katrina"),
    ("Show me records for Hurricane Harvey.", "Hurricane Harvey"),
    ("What information is available on Hurricane Harvey?", "Hurricane Harvey"),
    ("Find reports about Hurricane Ian.", "Hurricane Ian"),
    ("What records are available for Hurricane Ian?", "Hurricane Ian"),
    ("I need reports about the Camp Fire.", "Camp Fire"),
    ("What information is available about the Camp Fire?", "Camp Fire"),
    ("What studies mention the Northridge earthquake?", "Northridge earthquake"),
    ("Find records about the Northridge earthquake.", "Northridge earthquake"),
]

unsupported_tests = [
    "What information is available?",
    "Show me disaster reports.",
    "Find information about storms."
]


print("RULE-BASED EVENT EXTRACTION FEASIBILITY TEST")
print("=" * 52)

supported_correct = 0

for i, (question, expected) in enumerate(supported_tests, start=1):
    actual = extract_event(question)
    passed = actual == expected

    if passed:
        supported_correct += 1

    print(f"Supported Test {i}")
    print(f"Question: {question}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Result:   {'PASS' if passed else 'FAIL'}")
    print()

unsupported_correct = 0

for i, question in enumerate(unsupported_tests, start=1):
    actual = extract_event(question)
    passed = actual is None

    if passed:
        unsupported_correct += 1

    print(f"Unsupported Test {i}")
    print(f"Question: {question}")
    print("Expected: None")
    print(f"Actual:   {actual}")
    print(f"Result:   {'PASS' if passed else 'FAIL'}")
    print()

print("=" * 52)
print("SUMMARY")
print(f"Supported questions correct: {supported_correct}/{len(supported_tests)}")
print(f"Unsupported questions correctly rejected: {unsupported_correct}/{len(unsupported_tests)}")
