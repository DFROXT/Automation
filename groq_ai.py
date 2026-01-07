import os
from groq import Groq

# Groq client (API key Render ENV se aayegi)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script():
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Write a 30 second YouTube Shorts motivational script in simple English."
            }
        ]
    )
    return response.choices[0].message.content
