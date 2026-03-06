import json
import re
from pathlib import Path
from gpt4all import GPT4All

MODEL_PATH = Path(__file__).parent.parent / "models"

# Load model
model = GPT4All(
    "qwen2.5-coder-7b-instruct-q4_0.gguf",
    model_path=str(MODEL_PATH)
)


def generate_title_and_description(article_text: str):

    # Limit article size (small models struggle with long inputs)
    article_text = article_text[:2000]

    prompt = f"""
You are a professional news editor.

ARTICLE:
{article_text}

TASK:
Create a catchy news title and a short description.

Return ONLY valid JSON in this format:

{{
"title": "your title here",
"description": "your description here"
}}

Do not include explanations.
"""

    with model.chat_session():
        response = model.generate(prompt, max_tokens=150)

    print("\nRAW MODEL OUTPUT:")
    print(response)
    print("--------------------------------------------------")

    # Remove markdown fences if present
    response_clean = response.replace("```json", "").replace("```", "").strip()

    title = "Untitled"
    description = ""

    # Try strict JSON parsing
    try:
        parsed = json.loads(response_clean)
        title = parsed.get("title", "").strip()
        description = parsed.get("description", "").strip()

    except Exception:

        # Try extracting if model returns text instead of JSON
        match_title = re.search(r"(?:title|Title)\s*[:\-]\s*(.+)", response_clean)
        match_desc = re.search(r"(?:description|Description)\s*[:\-]\s*(.+)", response_clean)

        if match_title:
            title = match_title.group(1).strip()

        if match_desc:
            description = match_desc.group(1).strip()
        else:
            description = response_clean

    # Final cleanup
    title = re.sub(r"[{}\"]", "", title).strip()
    description = re.sub(r"[{}\"]", "", description).strip()

    return {
        "title": title if title else "Untitled",
        "description": description
    }