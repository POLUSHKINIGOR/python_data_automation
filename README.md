# Python Data Automation

This repository contains Python projects for data automation, including PDF extraction to CSV/Excel, JSON/CSV processing, web scraping with BeautifulSoup4 and Requests, and automation of repetitive tasks.

## Projects

### PDF to CSV/Excel
Extract structured data from PDF files and save as CSV or Excel.  
Libraries: `pdfplumber`, `csv`

```python
import pdfplumber
import csv

pdf_path = "path/to/your/file.pdf"
output_file = "output.csv"
all_text = []

# Extracting text from PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text.extend(text.split('\n'))

# Saving data directly to CSV without pandas
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow()  # Header
    for line in all_text:
        writer.writerow([line])

print(f"PDF data successfully saved to {output_file}")

### JSON to CSV/Excel
Clean and transform JSON data into CSV/Excel format.  
**Libraries:** `pandas`, `json`

```python
import json
import pandas as pd

json_path = "path/to/your/file.json"

# Reading JSON data with UTF-8 encoding
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Flattening JSON and saving to CSV
df = pd.json_normalize(data)
df.to_csv("output.csv", index=False)
print("JSON data successfully saved to output.csv")

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting all H1 and H2 tags from the page
    titles = soup.find_all(['h1', 'h2'])
    
    for title in titles:
        print(f"Found title: {title.get_text(strip=True)}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
```

# Python Data Automation

This repository contains Python projects for data automation, including PDF extraction to CSV/Excel, JSON/CSV processing, web scraping with BeautifulSoup4 and Requests, and automation of repetitive tasks.

## Projects

### 1. PDF to CSV/Excel
Extract structured data from PDF files and save them directly to CSV.  
**Libraries:** `pdfplumber`, `csv`

```python
import pdfplumber
import csv

pdf_path = "path/to/your/file.pdf"
output_file = "output.csv"
all_text = []

# Extracting text from PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text.extend(text.split('\n'))

# Saving data directly to CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["extracted_text"])
    for line in all_text:
        writer.writerow([line])

print(f"Data successfully saved to {output_file}")

import os
import shutil

# Path to folder for cleanup
folder_path = "path/to/folder"

# Remove all .tmp files
for filename in os.listdir(folder_path):
    if filename.endswith(".tmp"):
        os.remove(os.path.join(folder_path, filename))

# Move all .txt files to a subfolder
destination = os.path.join(folder_path, "txt_files")
os.makedirs(destination, exist_ok=True)
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        shutil.move(os.path.join(folder_path, filename), destination)

print("Automation tasks completed successfully")

import pdfplumber
import csv
from pathlib import Path

pdf_path = Path("document.pdf")
output_file = Path("output_tables.csv")

with pdfplumber.open(pdf_path) as pdf:
    all_rows = []
    for page in pdf.pages:
        # Extract data as a table structure (list of lists)
        table = page.extract_table()
        if table:
            all_rows.extend(table)

if all_rows:
    # utf-8-sig encoding ensures correct display in Excel
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(all_rows)
    print(f"Tables successfully saved to {output_file}")

### Web Scraping Demo
Scrape structured data from websites and extract structured information.  
**Libraries:** `requests`, `beautifulsoup4`, `pandas`

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com/data"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract table from the page
    table = soup.find("table")
    rows = []
    if table:
        for row in table.find_all("tr"):
            cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
            if cells:
                rows.append(cells)
    
    # Save to CSV
    df = pd.DataFrame(rows)
    df.to_csv("web_data.csv", index=False)
    print("Web data saved to CSV")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


