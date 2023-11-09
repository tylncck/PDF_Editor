from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def pdf_merger(pdf_file_list):
    merger = PdfWriter()

    for pdf in pdf_file_list:
        merger.append(pdf)
    
    merged_pdf_stream = BytesIO()
    merger.write(merged_pdf_stream)
    merged_pdf_stream.seek(0)
    
    return merged_pdf_stream


def pdf_compress(input_file):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    compressed_pdf_stream = BytesIO()
    writer.write(compressed_pdf_stream)
    compressed_pdf_stream.seek(0)
    return compressed_pdf_stream