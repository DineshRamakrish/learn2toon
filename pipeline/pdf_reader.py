import fitz

def extract_pdf_text(path: str) -> str:
    doc = fitz.open(path)
    pages = []
    for page in doc:
        pages.append(page.get_text("text"))
    return "\n\n".join(pages)
