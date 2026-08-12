import os
from openai import OpenAI

client = OpenAI()

def generate_narration(lesson: dict, audio_dir: str):
    for i, scene in enumerate(lesson["scenes"], 1):
        path = os.path.join(audio_dir, f"scene_{i:02d}.mp3")
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="coral",
            input=scene["narration"],
            instructions="Speak warmly and clearly like a friendly children's storyteller."
        ) as response:
            response.stream_to_file(path)
