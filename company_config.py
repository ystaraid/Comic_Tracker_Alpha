import ai_translation
import google.generativeai as genai
import os
from dotenv import load_dotenv
from ai_translation import get_english_answer

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def by_title(title):
    response = model.generate_content(f"if {title} is marvel, print marvel if it is dc, print dc if it is not marvel or dc, print other. do not include any additional information or explanation. only print the answer.")
    if response.text.strip() == "marvel":
        return "marvel"
    elif response.text.strip() == "dc":
        return "dc"
    else:
        return "other"

    