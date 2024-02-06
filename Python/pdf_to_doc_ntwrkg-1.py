# Import the PyPDF2 library
import PyPDF2


# Open the PDF file for reading
with open("E:\Misc\BSL00752-Pavithra-Harikhandige-Bhat-Contract-Extension-Letter_Scanned.pdf", "rb") as input_file:
    # Create a PdfReader object to read the PDF file
    pdf_reader = PyPDF2.PdfReader(input_file)

    # Open the Word document for writing
    with open("E:\Misc\BSL00752-Pavithra-Harikhandige-Bhat-Contract-Extension-Letter_Scanned.docx", "wb") as output_file:
        # Create a PdfWriter object to write the Word document
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through each page of the PDF file
        for page_num in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_num]

            # Add the page to the Word document
            pdf_writer.add_page(page)

        # Write the Word document
        pdf_writer.write(output_file)