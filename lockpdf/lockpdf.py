
import argparse
from PyPDF2 import PdfReader, PdfWriter
import os

def encrypt_pdf(input_pdf_path, password):
    """
    Encrypts a PDF file with the given password and saves the encrypted PDF
    with '-encrypted' appended to the original file name before the extension.
    
    :param input_pdf_path: Path to the input PDF file.
    :param password: Password to encrypt the PDF file.
    """
    # Generate output PDF path by appending '-encrypted' before the file extension
    file_name, file_extension = os.path.splitext(input_pdf_path)
    output_pdf_path = f"{file_name}-encrypted{file_extension}"
    
    # Initialize the PDF reader
    reader = PdfReader(input_pdf_path)
    
    # Initialize the PDF writer
    writer = PdfWriter()
    
    # Copy all pages from the reader to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    # Encrypt the PDF with the given password
    writer.encrypt(password)
    
    # Write the encrypted PDF to the output file
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)
        
    print(f"Encrypted PDF saved as: {output_pdf_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Encrypt a PDF file.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input PDF file.")
    parser.add_argument("-p", "--password", required=True, help="Password to encrypt the PDF file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Encrypt PDF
    encrypt_pdf(args.input, args.password)

if __name__ == "__main__":
    main()
    