# Python Data Automation

This project provides a set of Python scripts for automating routine tasks, including file management, data format conversion, and web scraping.

## 📁 Project Structure

### 1. Automation Scripts (`automation_scripts/`)
* **`automation_examples.py`**: Automatically renames and organizes `.txt` files into a dedicated `txt_files` folder.

### 2. JSON to CSV Converter (`json_to_csv/`)
* **`json_to_csv.py`**: Converts structured JSON data into a CSV file format, making it easy to open in Excel or Google Sheets.
    * **Input**: Looks for a `sample.json` file.
    * **Output**: Generates an `output.csv` with headers.

### 3. Additional Tools
* **pdf_to_csv/**: Scripts for extracting data from PDF files to CSV.
* **web_scraping_demo/**: Examples of extracting data from websites.

## 🛠️ Installation

To run the scripts in this repository, you need to have **Python 3.x** installed. You will also need to install the following dependencies:

```bash
pip install pandas requests beautifulsoup4 pdfplumber
```



