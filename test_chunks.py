from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text


with open("sample.pdf", "rb") as file:
    text = extract_text_from_pdf(file)

chunks = split_text(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)