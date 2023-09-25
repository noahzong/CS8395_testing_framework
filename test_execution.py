
import openai

# Set up the OpenAI API client with your API key
openai.api_key = 'YOUR_API_KEY'

def test_execution(description, input, header):
    """ 
    Queries the GPT-3 model to generate a solution based on the problem description.
    Then it runs the generated solution against the input data.
    """
    # Construct the prompt for the AI
    prompt = description + "Create a python function using the header given: " + header + " Run this function using the sample input: " + input
    
    # Query the AI model
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    
    # Extract the text from the AI's response
    ai_output = response.choices[0].text.strip()
    return ai_output
