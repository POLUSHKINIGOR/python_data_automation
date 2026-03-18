# Python Data Automation

This repository contains Python projects for data automation, including PDF extraction to CSV/Excel, JSON/CSV processing, web scraping, and automation of repetitive tasks.

## Projects

### PDF to CSV/Excel
Extract structured data from PDF files and save as CSV.  
**Libraries:** `pdfplumber`, `csv`

```python
import pdfplumber
import csv

pdf_path = "path/to/your/file.pdf"
output_file = "output.csv"
all_text = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text.extend(text.split('\n'))

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["extracted_text"])
    for line in all_text:
        writer.writerow([line])

print(f"PDF data successfully saved to {output_file}")



