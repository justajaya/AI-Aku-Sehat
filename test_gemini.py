import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = (os.getenv("GEMINI_MODEL") or "gemini-3.8-flash").removeprefix("models/")

# 2.5 Flash access is currently restricted for many new users/projects.
# Normalize old local configuration to the current Flash model.
legacy = {
    "gemini-2.5-flash": "gemini-3.8-flash",
    "gemini-2.0-flash": "gemini-3.8-flash",
}
model = legacy.get(model, model)

if not api_key:
    raise SystemExit("GEMINI_API_KEY belum ada di .env")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model=model,
    contents="Balas hanya dengan: GEMINI_OK",
)

print("Model:", model)
print("Response:", (response.text or "").strip())
