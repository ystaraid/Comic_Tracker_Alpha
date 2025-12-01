import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def get_korean_answer(question):
    response = model.generate_content(question)
    translated_text = model.generate_content(f"{response.text} \n Translate this to Korean. Do not include any additional information other than the translation. ")
    return translated_text.text 

def get_english_answer(question):
    response = model.generate_content(question)
    translated_text = model.generate_content(f"{response.text} \n Translate this to English. Do not include any additional information other than the translation. ")
    return translated_text.text 


