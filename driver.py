
from test_framework import read_tests_from_file, run_tests, calculate_score
from test_execution import test_execution

def main():
    # Read tests from the sample file
    tests = read_tests_from_file("sample_tests.json")
    
    # Run the tests using the test execution function
    passed_tests, total_tests = run_tests(tests, test_execution)
    
    # Calculate the score
    score = calculate_score(passed_tests, total_tests)
    
    print(f"Passed {passed_tests} out of {total_tests} tests. Score: {score:.2f}%")

if __name__ == "__main__":
    main()
