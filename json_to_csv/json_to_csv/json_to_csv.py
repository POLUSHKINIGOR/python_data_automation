import json
import csv
import os

# Example JSON file path (put your JSON in the same folder as this script)
json_file_path = os.path.join(os.getcwd(), "sample.json")
csv_output_path = os.path.join(os.getcwd(), "output.csv")

# Load JSON data
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Assume JSON is a list of dictionaries
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    # Get CSV headers from keys of the first dictionary
    headers = data[0].keys()
    
    # Write to CSV
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"JSON '{json_file_path}' successfully converted to CSV '{csv_output_path}'")
else:
    print("JSON structure is not a list of dictionaries. Please check your JSON file.")
