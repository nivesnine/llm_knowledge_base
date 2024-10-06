# run_test.py
import os
import sys
import uuid
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def run_baseline_test(prompt, model_name):
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    model = genai.GenerativeModel(model_name=model_name)
    response = model.generate_content([prompt])
    return response.text.strip()

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
        model_name = "gemini-1.5-flash"


    with open(input_file, 'r') as f:
        prompts = f.readlines()

    for prompt in prompts:
        result = run_baseline_test(prompt, model_name)
        with open(output_file, 'a') as result_file:
            result_file.write(f"# Prompt: {prompt}\nResponse:\n\n{result}\n---\n")
        print(f"Tested prompt: {prompt.strip()}")