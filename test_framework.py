
import json

def read_tests_from_file(filename):
    """ Reads a JSON file containing a list of test objects and returns the list. """
    with open(filename, 'r') as file:
        tests = json.load(file)
    return tests

def run_tests(tests, test_execution_function):
    total_tests = 0
    passed_tests = 0

    for test in tests:  
        for test_case in test["test_cases"]:
            total_tests += 1
            actual_output = test_execution_function(test["description"], test_case["input"], test["sample_header"])
            print(actual_output)
            print("break")
            if actual_output == test_case["expected_output"]:
                passed_tests += 1

    return passed_tests, total_tests

def calculate_score(passed_tests, total_tests):
    if total_tests == 0:
        return 0
    return (passed_tests / total_tests) * 100
