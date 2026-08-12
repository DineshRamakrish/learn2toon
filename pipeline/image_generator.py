import os
from openai import OpenAI

client = OpenAI()

STYLE = (
    "Cute polished 2D children's educational cartoon, warm friendly expressions, "
    "bright classroom/storybook feel, clean shapes, consistent character design, "
    "soft cinematic lighting, no written words, no captions, no logos."
)

def generate_scene_images(lesson: dict, image_dir: str):
    for i, scene in enumerate(lesson["scenes"], 1):
        prompt = STYLE + "\n" + scene["visual_prompt"]

        result = client.images.generate(
            model="gpt-image-2",
            prompt=prompt,
            size="1536x1024",
            quality="medium"
        )

        image_b64 = result.data[0].b64_json
        import base64
        path = os.path.join(image_dir, f"scene_{i:02d}.png")
        with open(path, "wb") as f:
            f.write(base64.b64decode(image_b64))
