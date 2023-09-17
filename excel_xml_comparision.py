import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xml.etree.ElementTree as ET

def choose_excel_file():
    excel_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    excel_file_entry.delete(0, tk.END)
    excel_file_entry.insert(0, excel_file_path)

def choose_xml_file():
    xml_file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    xml_file_entry.delete(0, tk.END)
    xml_file_entry.insert(0, xml_file_path)

def compare_files():
    excel_file_path = excel_file_entry.get()
    xml_file_path = xml_file_entry.get()

    # Read Excel file
    excel_data = pd.read_excel(excel_file_path)
    
    # Read XML file
    xml_tree = ET.parse(xml_file_path)
    xml_root = xml_tree.getroot()

    # Define column-key mappings
    mappings = {}
    for mapping_entry in mappings_entries:
        column = mapping_entry[0].get()
        key = mapping_entry[1].get()
        if column and key:
            mappings[column] = key

    # Compare data
    for index, row in excel_data.iterrows():
        for column, key in mappings.items():
            excel_value = row[column]
            xml_element = xml_root.find(key)
            if xml_element is not None and xml_element.text != excel_value:
                print(f"Mismatch found at row {index+2}, column {column}:")
                print(f"Excel value: {excel_value}")
                print(f"XML value: {xml_element.text}")
                print("=" * 40)

# Create the main window
window = tk.Tk()
window.title("Excel-XML Data Comparison")

# Excel file selection
excel_file_label = tk.Label(window, text="Excel File:")
excel_file_label.grid(row=0, column=0, padx=10, pady=10)
excel_file_entry = tk.Entry(window, width=50)
excel_file_entry.grid(row=0, column=1, padx=10, pady=10)
excel_file_button = tk.Button(window, text="Browse", command=choose_excel_file)
excel_file_button.grid(row=0, column=2, padx=10, pady=10)

# XML file selection
xml_file_label = tk.Label(window, text="XML File:")
xml_file_label.grid(row=1, column=0, padx=10, pady=10)
xml_file_entry = tk.Entry(window, width=50)
xml_file_entry.grid(row=1, column=1, padx=10, pady=10)
xml_file_button = tk.Button(window, text="Browse", command=choose_xml_file)
xml_file_button.grid(row=1, column=2, padx=10, pady=10)

# Mapping entries
mappings_entries = []
mapping_label = tk.Label(window, text="Column-Key Mappings:")
mapping_label.grid(row=2, column=0, padx=10, pady=10)
add_mapping_button = tk.Button(window, text="Add Mapping", command=lambda: add_mapping_entry())
add_mapping_button.grid(row=2, column=1, padx=10, pady=10)

def add_mapping_entry():
    column_entry = tk.Entry(window, width=20)
    column_entry.grid(row=3 + len(mappings_entries), column=0, padx=10, pady=5)
    key_entry = tk.Entry(window, width=20)
    key_entry.grid(row=3 + len(mappings_entries), column=1, padx=10, pady=5)
    mappings_entries.append((column_entry, key_entry))

# Compare button
compare_button = tk.Button(window, text="Compare", command=compare_files)
compare_button.grid(row=3 + len(mappings_entries), column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()