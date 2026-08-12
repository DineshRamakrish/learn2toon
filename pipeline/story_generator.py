import json
from openai import OpenAI

client = OpenAI()

def create_lesson(text: str, age: str, language: str) -> dict:
    # Keep the first MVP bounded. Increase later with chunking/summarisation.
    text = text[:30000]

    prompt = f'''
You are creating an educational cartoon video for children aged {age}.
Read the source material below and create 5 to 8 short scenes.

Return ONLY valid JSON:
{{
  "title": "...",
  "scenes": [
    {{
      "title": "...",
      "narration": "2-4 child-friendly sentences.",
      "visual_prompt": "A consistent 2D children's cartoon scene. Describe characters,
      setting, action, educational concept, and composition. No text in the image."
    }}
  ]
}}

Rules:
- Preserve the factual meaning of the source.
- Do not invent facts that are not needed.
- Use simple language appropriate for the age.
- Make the lesson feel like a story.
- Keep visual style consistent across all scenes.
- No frightening, violent, or inappropriate content.
- Language: {language}

SOURCE:
{text}
'''

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    raw = response.output_text
    return json.loads(raw)
