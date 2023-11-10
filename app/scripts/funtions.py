from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
import os

def save_file(file_uploader):
    target_directory = 'app/files'
    os.makedirs(target_directory, exist_ok=True)
    target_path = os.path.join(target_directory, file_uploader.name)
    with open(target_path, "wb") as file:
        file.write(file_uploader.read())
    return target_path

def delete_pdf_files():
    target_directory = 'app/files'
    files = os.listdir(target_directory)
    pdf_files = [file for file in files if file.lower().endswith(".pdf")]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(target_directory, pdf_file)
        os.remove(pdf_path)

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

def get_pdf_page_count(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        return len(pdf_reader.pages)

def pdf_inserter(pdf1, pagerange1, pdf2, pagerange2, position):
    merger = PdfWriter()

    file1 = open(pdf1, "rb")
    file2 = open(pdf2, "rb")

    # add pages from the first PDF file to output file as a whole
    merger.append(fileobj=file1, pages = pagerange1)

    # insert the pages  of input2 into the output beginning after the second page
    merger.merge(position=position, fileobj=file2, pages=pagerange2)

    inserted_pdf_stream = BytesIO()
    merger.write(inserted_pdf_stream)
    inserted_pdf_stream.seek(0)
    return inserted_pdf_stream