import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

from pipeline.pdf_reader import extract_pdf_text
from pipeline.story_generator import create_lesson
from pipeline.image_generator import generate_scene_images
from pipeline.voice_generator import generate_narration
from pipeline.video_generator import build_video

load_dotenv()

st.set_page_config(page_title="Book to Cartoon", page_icon="🎬")
st.title("📚 → 🎬 Book to Cartoon")
st.write("Upload a learning PDF and turn it into a short, child-friendly animated lesson.")

pdf = st.file_uploader("Upload PDF", type=["pdf"])
age = st.selectbox("Child age", ["5-7", "8-10", "11-13"])
language = st.selectbox("Narration language", ["English"])

if pdf and st.button("Create Cartoon Video", type="primary"):
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Set OPENAI_API_KEY in .env first.")
        st.stop()

    with tempfile.TemporaryDirectory() as work:
        pdf_path = os.path.join(work, "book.pdf")
        with open(pdf_path, "wb") as f:
            f.write(pdf.getbuffer())

        with st.status("Creating your video...", expanded=True) as status:
            st.write("📖 Reading PDF...")
            text = extract_pdf_text(pdf_path)

            if not text.strip():
                st.error("No selectable text was found. This MVP needs a text-based PDF.")
                st.stop()

            st.write("🧠 Creating child-friendly scenes...")
            lesson = create_lesson(text, age, language)

            st.write(f"🎨 Generating {len(lesson['scenes'])} cartoon scenes...")
            image_dir = os.path.join(work, "images")
            os.makedirs(image_dir, exist_ok=True)
            generate_scene_images(lesson, image_dir)

            st.write("🗣️ Generating narration...")
            audio_dir = os.path.join(work, "audio")
            os.makedirs(audio_dir, exist_ok=True)
            generate_narration(lesson, audio_dir)

            st.write("🎬 Rendering MP4...")
            output = os.path.join(work, "cartoon_lesson.mp4")
            build_video(lesson, image_dir, audio_dir, output)

            final_output = os.path.join("output", "cartoon_lesson.mp4")
            os.makedirs("output", exist_ok=True)
            with open(output, "rb") as src, open(final_output, "wb") as dst:
                dst.write(src.read())

            status.update(label="Video ready!", state="complete")

    st.video(final_output)
    with open(final_output, "rb") as f:
        st.download_button("⬇️ Download MP4", f, "cartoon_lesson.mp4", "video/mp4")
