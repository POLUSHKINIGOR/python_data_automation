import pdfplumber
import csv
import os

# Example PDF file path (put your PDF in the same folder as this script)
pdf_file_path = os.path.join(os.getcwd(), "sample.pdf")
csv_output_path = os.path.join(os.getcwd(), "output.csv")

# Open the PDF and extract text
with pdfplumber.open(pdf_file_path) as pdf:
    all_text = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text.append(text)

# Split text into lines and prepare for CSV
csv_lines = []
for page_text in all_text:
    for line in page_text.split('\n'):
        csv_lines.append([line])

# Write to CSV
with open(csv_output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_lines)

print(f"PDF '{pdf_file_path}' has been successfully converted to CSV '{csv_output_path}'")
