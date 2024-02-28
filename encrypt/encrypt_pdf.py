import argparse
import pikepdf


def encrypt_pdf(input_file, password):
    # Open the input PDF
    pdf = pikepdf.Pdf.open(input_file)

    # Define the output file name
    output_file = f"{input_file.rsplit('.', 1)[0]}-encrypted.pdf"

    # Save the PDF with encryption
    pdf.save(output_file, encryption=pikepdf.Encryption(owner=password, user=password, R=6))

    # Close the PDF
    pdf.close()

    print(f"File encrypted successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Encrypt a PDF file.')
    parser.add_argument('-i', '--input', required=True, help='Input PDF file to encrypt.')
    parser.add_argument('-p', '--password', required=True, help='Password for encryption.')
    args = parser.parse_args()

    encrypt_pdf(args.input, args.password)


if __name__ == "__main__":
    main()
