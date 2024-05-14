# PNM3HC10/05/2024 : Parse data from excel file to txt base on template
#   How it work ? 
#   Each key word map with one column in excel file
#   Each row in excel file will create a new paragraph exactly same with the template then replace the keywords with data in excel file.
#   Afterward it will output all paragraphs in one output.txt file

import openpyxl
import re
from openpyxl.utils import get_column_letter, column_index_from_string

def get_cell(extract_cell):
    for i in range (len(extract_cell)):
        if extract_cell[i] == '.':
            cell_c = extract_cell[i+1:-1]
            break
    num = re.findall(r'\d+', cell_c)
    char = cell_c.replace(num[0],'')
    row_max = int(num[0])
    col_max = int(column_index_from_string(char))
    return row_max, col_max


output_text = ''

template_file_name = str(input('template file (txt file): '))
excel_file_name = str(input('Excel file name : '))
start_row = int(input('Start row : '))


lines = []
specific_string = "stop"

# Read the template file
with open(template_file_name, 'r') as template_file:
    template = str(template_file.read())




# Read the Excel file and extract data
workbook = openpyxl.load_workbook(excel_file_name)
sheet = workbook.active

extract_cell = str(sheet[1][-1])
row_max, col_max = get_cell(extract_cell)
extract_cell = str(sheet[get_column_letter(col_max)][-1])
row_max, col_max = get_cell(extract_cell)





while True:
    line = input("Enter a mapping '[substring] [Excel column]' Ex: 'DID A' (type 'stop' to end): ")
    if line == specific_string:
        break
    line_values = line.split()
    lines.append(line_values)
print(len(lines))
print('\n')
for row in range (start_row,row_max):
    temp = "\n" + template
    for i in range(len(lines)):
        col = lines[i][1]
        # logic here
        temp_val = str(sheet[col][row].value)
        temp = temp.replace(lines[i][0], temp_val)

    output_text = output_text + temp


# Write the modified content to a new text file
with open('output.txt', 'w') as output_file:
    output_file.write(output_text)

print("File created successfully!")