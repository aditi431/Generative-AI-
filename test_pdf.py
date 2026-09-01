from utils.pdf_loader import extract_text_from_pdf


pdf_path = "sample.pdf"

with open(pdf_path, "rb") as file:
    text = extract_text_from_pdf(file)

print(text[:3000])