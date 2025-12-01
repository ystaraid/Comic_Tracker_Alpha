import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# API 키 설정
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 모델 설정 (gemini-1.5-flash 또는 gemini-1.5-pro 사용 권장)
model = genai.GenerativeModel('gemini-2.0-flash')

# 3. 질문 보내기
response = model.generate_content("if fantastic four is marvel, print marvel if it is dc, print dc if it is not marvel or dc, print other")

# 4. 답변 출력
print(response.text)