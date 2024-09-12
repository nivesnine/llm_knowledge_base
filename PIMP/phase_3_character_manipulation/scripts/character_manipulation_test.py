# manipulation_test.py
import openai

# Set your OpenAI API key
api_key = "your-api-key-here"
openai.api_key = api_key

def run_manipulation_test(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error during API call: {e}"

if __name__ == "__main__":
    # Load manipulation test prompts from a file
    with open('manipulation_prompts.md', 'r') as f:
        prompts = f.readlines()

    # Run the test for each manipulated prompt and save the result
    for prompt in prompts:
        result = run_manipulation_test(prompt)
        with open('manipulation_results.md', 'a') as result_file:
            result_file.write(f"Prompt: {prompt}\nResponse: {result}\n\n")
        print(f"Tested manipulated prompt: {prompt.strip()}")