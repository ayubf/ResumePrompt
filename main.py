import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

with open('private.json', 'r') as file:
    data = json.load(file)
    contact_info = data.get('contact_info')

with open('prompt.md', 'r') as file:
    prompt_template = file.read()
prompt_filled = prompt_template.replace('{contact_info}', contact_info)

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-2.0-flash")
resp = model.generate_content(prompt_filled)

lines = resp.text.splitlines()
trimmed = "\n".join(lines[1:-1]) if len(lines) >= 2 else resp.text

os.makedirs('output', exist_ok=True)
with open('output/resume.tex', 'w') as file:
    file.write(trimmed)