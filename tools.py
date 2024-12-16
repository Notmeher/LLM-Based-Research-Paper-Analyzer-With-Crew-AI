import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    """
    Extracts all text from the provided PDF file.
    """
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return None
