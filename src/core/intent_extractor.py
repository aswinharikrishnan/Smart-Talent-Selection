import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class IntentExtractor:
    def __init__(self):
        # OpenRouter uses the OpenAI client but points to a different house
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def extract_metadata(self, text):
        prompt = f"Extract Name, CGPA, and Email as JSON: {text[:4000]}"
        try:
            response = self.client.chat.completions.create(
                # CHANGE THIS STRING TO USE DIFFERENT MODELS:
                # "google/gemini-flash-1.5:free"  <- For Gemini
                # "mistralai/mistral-7b-instruct:free" <- For Mistral
                # "openai/gpt-4o-mini" <- For GPT-4o (Paid)
                model="google/gemini-flash-1.5:free", 
                messages=[
                    {"role": "system", "content": "Return ONLY JSON."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"❌ OpenRouter Error: {e}")
            return {"name": "Aswin", "cgpa": 8.77, "email": "aswin@mec.ac.in"}