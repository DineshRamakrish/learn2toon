import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def build_video(lesson: dict, image_dir: str, audio_dir: str, output: str):
    clips = []

    for i, _scene in enumerate(lesson["scenes"], 1):
        image = os.path.join(image_dir, f"scene_{i:02d}.png")
        audio = os.path.join(audio_dir, f"scene_{i:02d}.mp3")

        audio_clip = AudioFileClip(audio)
        duration = audio_clip.duration + 0.25

        clip = (
            ImageClip(image)
            .with_duration(duration)
            .resized(height=720)
            .with_audio(audio_clip)
        )
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        logger=None
    )

    final.close()
    for clip in clips:
        clip.close()
