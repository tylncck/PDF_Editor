# PDF Editor Application

This is a simple PDF Editor Application that allows users to perform various operations on PDF files, such as merging, compressing, splitting, and inserting one PDF into another. The application is built using Streamlit and leverages the PyPDF2 library for PDF manipulation.

## Docker Container

### Installation
To run the application, make sure you have Docker Desktop installed on your system. Plase visit [Docker Website](https://docs.docker.com/desktop/) for more information. 

### Building and Running the Container
1. Open a terminal, navigate to a desired directory to clone this repository. Run `git clone https://github.com/tylncck/PDF_Editor.git`. For this task git must be installed on your local machine. Please follow [Git Website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for more details. 
2. This repository comes with `docker-compose.yml` file. All you need is to run `docker compose up --build` command on your terminal or VSCode terminal. 
3. Alternatively you can build and run the container with following commands: `docker build -t pdf-editor-app` then `docker run -p 8501:8501 pdf-editor-app`
4. Open your browser and navigate to the Network URL prompted on the terminal to access the PDF Editor Application. The url may be like [http://localhost:8501/app](http://localhost:8501/app) or a URL containing an IP number followed by the assigned port. 

## Application Pages

### Home Page
- Welcoming message and navigation instructions.

### PDF Merger Page
- Upload and merge multiple PDF files into one PDF file.

### PDF Compression Page
- Upload and compress a PDF file to reduce its size. Performance depends on the content of the uploaded file. 

### PDF Slicer Page
- Upload and slice a PDF file to only get some pages and use these pages to create a new PDF file.

### PDF Inserter Page
- Upload two PDF files and insert the second file after a specified page of the first file. Files can be used with all pages or you can decide which pages to use. 

### Watermarking Page
- Upload a PDF file and add a watermark with determined text, color, and position. (Currently *Confidential* and *Do Not Copy* version are available.)

## Credits
- The application utilizes the [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) library for PDF manipulation. 

- Ghostscript is used for PDF compression. Visit [Ghostscript](https://www.ghostscript.com/) for more information.

Credits to the PyPDF2 and Ghostscript developers for their contribution to open source habitat. 

## Conclusion
This PDF Editor Application provides a user-friendly interface for common PDF editing tasks. Feel free to explore and enhance your PDFs seamlessly!
I'll try my best to add new features to the application. 

by tylncck