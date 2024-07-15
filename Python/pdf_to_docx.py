import os
os.system('whoami')
from pdf2docx import Converter

def pdf_to_docx(input_pdf, output_docx, selected_pages=None, page_range=None):
    if selected_pages is not None and page_range is not None:
        raise ValueError("Please select either 'selected_pages' or 'page_range', not both.")

    cv = Converter(input_pdf)
    if selected_pages is not None:
        page_list = [int(page) for page in selected_pages.split(',')]
        cv.convert(output_docx, pages=page_list)
    elif page_range is not None:
        start, end = map(int, page_range.split('-'))
        cv.convert(output_docx, start=start, end=end)
    else:
        cv.convert(output_docx)

    cv.close()

#Usage:
pdf_file = 'E:\\Misc\\Sri_Hanuman_Chalisa_English.pdf'
docx_file = 'E:\\Misc\\docx'

#Choose either selected pages or page range
selected_pages = '1, 3'
#selected_pages = None
page_range = None
#page_range = '1-3'

pdf_to_docx(pdf_file, docx_file, selected_pages=selected_pages, page_range=page_range)