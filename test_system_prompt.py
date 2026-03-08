import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    
    prompt = "What is 2+2?"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[types.Content(role="user", parts=[types.Part(text=prompt)])],
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    
    print(f"User asked: {prompt}")
    print(f"System instruction: {system_prompt}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
