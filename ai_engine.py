import os
from openai import OpenAI
from system_prompt import build_system_prompt

def ask_electrical_ai(question: str, language: str):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "AI service is not configured. Please add a valid API key."

    try:
        client = OpenAI(api_key=api_key)

        messages = [
            {
                "role": "system",
                "content": build_system_prompt(language)
            },
            {
                "role": "user",
                "content": question
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=600
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I faced a technical issue. Please try again.\n\nDetails: {str(e)}"
