import requests
from bs4 import BeautifulSoup
import csv
import os

# Example URL to scrape
url = "https://example.com/sample-page"

# Output CSV file path
csv_output_path = os.path.join(os.getcwd(), "web_scraping_output.csv")

# Send GET request to the page
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Example: extract all rows from a table
table = soup.find("table")  # assumes there is a <table> on the page
if not table:
    print("No table found on the page.")
    exit()

rows = table.find_all("tr")
csv_data = []
for row in rows:
    cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
    csv_data.append(cols)

# Write to CSV
with open(csv_output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print(f"Data from '{url}' successfully saved to CSV '{csv_output_path}'")
