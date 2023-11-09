import streamlit as st
from scripts.funtions import pdf_compress
import subprocess
import io 
import os

st.title('Compressing PDFs')

# Create a radio button to choose the compression method
compression_method = st.radio("Select Compression Method", ("PyPDF2 Compression", "Ghostscript Compression"))

uploaded_file = st.file_uploader('Upload your PDF files (multiple files supported)', type=['pdf'], accept_multiple_files=False)

if uploaded_file:
    if st.button('Compress PDF'):
        output_file_name = uploaded_file.name.replace('.pdf', '_compressed.pdf')
        if compression_method == "PyPDF2 Compression":
            compressed_pdf = pdf_compress(uploaded_file)
        else:
            target_directory = 'app/files'
            os.makedirs(target_directory, exist_ok=True)

            target_path = os.path.join(target_directory, uploaded_file.name)
            with open(target_path, "wb") as file:
                file.write(uploaded_file.read())
            
            output_file = target_directory + '/' + output_file_name
            
            compression_command = f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_file}" "{target_path}"'
            
            subprocess.run(compression_command, shell=True, check=True)
            
            with open(output_file, 'rb') as f:
                compressed_pdf = io.BytesIO(f.read())

        uploaded_file_size = len(uploaded_file.getvalue()) / (1024 * 1024)
        compressed_file_size = len(compressed_pdf.getvalue()) / (1024 * 1024)

        st.write(f'Compressed the uploaded PDF successfully using the {compression_method}. Initial file size {uploaded_file_size:.2f} MB reduced to {compressed_file_size:.2f} MB. Click the button to download the compressed file.')

        # Remove the saved files
        files = os.listdir(target_directory)

        # Filter PDF files
        pdf_files = [file for file in files if file.lower().endswith(".pdf")]

        # Remove PDF files
        for pdf_file in pdf_files:
            pdf_path = os.path.join(target_directory, pdf_file)
            os.remove(pdf_path)

        st.download_button('Download Compressed PDF', compressed_pdf, key='download_pdf', file_name=output_file_name)

