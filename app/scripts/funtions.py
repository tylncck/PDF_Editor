from PyPDF2 import PdfWriter
from io import BytesIO

def pdf_merger(pdf_file_list):
    merger = PdfWriter()

    for pdf in pdf_file_list:
        merger.append(pdf)
    
    merged_pdf_stream = BytesIO()
    merger.write(merged_pdf_stream)
    merged_pdf_stream.seek(0)
    
    return merged_pdf_stream