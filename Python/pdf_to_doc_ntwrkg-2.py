import PyPDF2
from docx import Document

def pdf_to_doc(input_pdf_path, output_doc_path):
    pdf = PyPDF2.PdfReader(input_file_path)
    doc = Document()

    for page_num in range(len(pdf.numPages)):
        page = pdf.getPage[page_num]
        text = page.extractText()
        doc.add_paragraph(text)

    doc.save(f"PDF Successfully converted to Word Document. Output saved at: {output_doc_path}")

    #Usage:
    input_pdf_path ="E:\Misc\BSL00752-Pavithra-Harikhandige-Bhat-Contract-Extension-Letter_Scanned.pdf"
    output_doc_path = "E:\Misc\BSL00752-Pavithra-Harikhandige-Bhat-Contract-Extension-Letter_Scanned.docx"
    pdf_to_doc(input_pdf_path, output_doc_path)