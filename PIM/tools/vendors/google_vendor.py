import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

load_dotenv()

class GoogleVendor:
    def __init__(self):
        self.default_model_name = "gemini-1.5-flash-8b"
        

    def run(self, prompt, model_name):
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        try:
            model = genai.GenerativeModel(model_name=model_name)
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error during API call: {e}")
            return "Failed to generate resspose"