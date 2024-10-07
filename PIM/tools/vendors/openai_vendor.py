import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIVendor:
    def __init__(self):
        self.default_model_name = "gpt-4o-2024-08-06"

    def run(self, prompt, model_name):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        try:
            response = client.completions.create(
                model=model_name,
                prompt=prompt
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error during API call: {e}")
            return "Failed to generate resspose"