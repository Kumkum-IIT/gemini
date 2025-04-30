from openai import OpenAI

client = OpenAI(
    api_key="API Key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-1.5-flash",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
