# CS8395_testing_framework
Generated using ChatGPT

**1. Setup:**
Required Software:
Python (preferably Python 3.6 or newer).
openai Python library if you're using the OpenAI API integration.
Installation:
Install the openai library using pip install openai

**2. Files Overview:**
test_framework.py: Contains the main framework functions for reading tests, executing them, and calculating scores.
test_execution_with_api.py: Contains the function that prompts the GPT AI to generate a solution based on the problem description.
driver.py: The main script to run the tests and display results.
sample_tests_v3.json: Sample test cases stored in JSON format.

**3. Configuring API Key:**
openai.api_key = 'YOUR_OPENAI_API_KEY' (Located in test_execution.py)
Replace 'YOUR_OPENAI_API_KEY' with your actual API key.

**4. Writing Tests:**
Edit sample_tests.json or create a new JSON file to include your tests. The structure should be:
[
    {
        "test_name": "Name of the Test",
        "description": "Description or prompt for the AI",
        "sample_header": "Optional. Sample header or context for test cases.",
        "test_cases": [
            {"input": "input_data", "expected_output": "expected_output_data"},
            ...
   ]
    },
    ...
]

**5. Running Tests:**
Navigate to the directory containing the files in your terminal or command prompt. Then, run:
python driver.py

**6. Review Results:**
The script will display the number of passed tests, total tests, and the overall score as a percentage.

**7. Modifying Test Execution Logic:**
If you want to use a different logic or method for test execution, modify the test_execution function in test_execution_with_api.py (or a similar file). This function receives the input data and the problem description and should return the output.

**8. Further Customization:**
When using different AI models, modify the test execution function, replacing the call to the OpenAI API with a call to the desired AI model's API.

