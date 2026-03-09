from dotenv import load_dotenv
load_dotenv()
import os
from google import genai

try:
    client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[{'role': 'user', 'parts': [{'text': 'test'}]}]
    )
    print('✅ API working - quota likely reset')
except Exception as e:
    if '429' in str(e) or 'RESOURCE_EXHAUSTED' in str(e):
        print('❌ Still quota limited')
    else:
        print(f'⚠️ Other error: {e}')
