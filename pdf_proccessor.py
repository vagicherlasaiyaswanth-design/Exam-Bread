import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_file):
    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text

if __name__ == "__main__":
    with open("sample.pdf", "rb") as file:
        text = extract_text_from_pdf(file)

    print(text)
