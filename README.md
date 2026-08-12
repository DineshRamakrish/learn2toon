# Learn2Toon 🎬📚

**Turn educational books and PDFs into short, child-friendly cartoon learning videos.**

Learn2Toon takes educational content and turns it into:
- 🧠 Simple, age-appropriate lesson scripts
- 🎨 Cartoon learning scenes
- 🗣️ Friendly AI narration
- 🎬 A downloadable MP4 lesson

## Architecture

```text
PDF
 ↓
PDF Text Extraction
 ↓
AI Lesson / Scene Generation
 ↓
Cartoon Image Generation
 ↓
AI Narration
 ↓
Video Assembly
 ↓
🎬 Learning Video
```

## Project Structure

```text
learn2toon/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── pipeline/
│   ├── pdf_reader.py
│   ├── story_generator.py
│   ├── image_generator.py
│   ├── voice_generator.py
│   └── video_generator.py
├── assets/
└── output/
```

## Run locally

### 1. Clone

```bash
git clone <your-repository-url>
cd learn2toon
```

### 2. Create environment

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI

Copy `.env.example` to `.env`:

```text
OPENAI_API_KEY=your_api_key_here
```

Never commit `.env` or your API key.

### 5. Install FFmpeg

FFmpeg must be installed and available on your system PATH.

### 6. Start the app

```bash
streamlit run app.py
```

Upload a text-based PDF and select the target age group.

## Current MVP

The current version supports:

- Text-based PDF extraction
- AI scene/story generation
- Cartoon scene image generation
- AI narration
- MP4 generation
- Streamlit upload/download interface

## Planned Improvements

- OCR for scanned PDFs
- Consistent characters across scenes
- Subtitles
- Background music
- Interactive quizzes
- Multiple languages
- Better page/chapter selection
- Automatic educational illustrations
- Child-safe content controls
- Cloud deployment

## Responsible Use

Only upload content you have permission to process. This project is intended for educational content generation and should not replace professional advice or authoritative educational/medical guidance.
