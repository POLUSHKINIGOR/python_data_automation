# Python Data Automation

This repository contains a collection of Python scripts designed to automate routine data management, file system tasks, and data conversion.

## 📁 Project Structure

### 1. Automation Scripts (`automation_scripts/`)
* **`automation_examples.py`**: Automatically renames and organizes `.txt` files into a dedicated `txt_files` folder.

### 2. JSON to CSV Converter (`json_to_csv/`)
* **`json_to_csv.py`**: Converts structured JSON data into a CSV file format for easy analysis.
    * **Input**: Looks for a `sample.json` file.
    * **Output**: Generates an `output.csv`.

### 3. PDF to CSV Converter (`pdf_to_csv/`)
* **`pdf_to_csv.py`**: Extracts text content from PDF documents and saves it into a CSV file using the `pdfplumber` library.
    * **Input**: Uses `sample.pdf` from the current directory.
    * **Output**: Generates a structured `output.csv`.

### 4. Web Scraping Demo (`web_scraping_demo/`)
* Examples of extracting data from websites for further analysis or storage.

## 🛠️ Installation

To run the scripts, you need **Python 3.x**. Install the necessary dependencies:

```bash
pip install pandas requests beautifulsoup4 pdfplumber
```



