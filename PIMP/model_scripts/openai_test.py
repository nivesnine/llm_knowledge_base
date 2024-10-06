# openai_test.py
import os
import sys
import uuid
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def run_baseline_test(prompt, model_name):
    try:
        response = client.completions.create(
            model=model_name,
            prompt=prompt
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error during API call: {e}"

if __name__ == "__main__":
    if "-i" in sys.argv:
        input_file = sys.argv[sys.argv.index("-i") + 1]
    else:
        input_file = '../tests/prompts.txt'

    if "-o" in sys.argv:
        output_file = sys.argv[sys.argv.index("-o") + 1]
    else:
        unique_filename = str(uuid.uuid4())
        output_file = '../results/' + unique_filename + '.md'

    if "-m" in sys.argv:
        model_name = sys.argv[sys.argv.index("-m") + 1]
    else:
        model_name = "gpt-4o-2024-08-06"


    # Load baseline test prompts from a file
    with open(input_file, 'r') as f:
        prompts = f.readlines()

    # Run the test for each prompt and save the result
    for prompt in prompts:
        result = run_baseline_test(prompt, model_name)
        with open(output_file, 'a') as result_file:
            result_file.write(f"# Prompt: {prompt}\nResponse:\n\n{result}\n---\n")
        print(f"Tested prompt: {prompt.strip()}")