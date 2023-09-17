import os
import datetime
import openpyxl
import re

def detect_misra_violations(file_path):
    violations = []

    # Rule 2.1
    for line_number, line in enumerate(open(file_path, 'r'), start=1):
        if re.search(r'\bfor\s*\(.*;.*;.*\)', line):
            violations.append({
                'Rule': '2.1',
                'Line': line_number,
                'Detail': 'The essentials of the plain \'for\' statement shall not be bypassed.',
                'Solution': 'Review and modify the \'for\' loop to ensure it adheres to the rule.',
            })

    # Rule 2.2
    if '/*UNREACHABLE*/' in open(file_path).read():
        violations.append({
            'Rule': '2.2',
            'Line': None,
            'Detail': 'A project shall not contain unreachable code.',
            'Solution': 'Identify and remove unreachable code segments in the project.',
        })

    # Rule 2.3
    if 'typedef' in open(file_path).read() and 'UNUSED_TYPE' in open(file_path).read():
        violations.append({
            'Rule': '2.3',
            'Line': None,
            'Detail': 'A project shall not contain unused type declarations.',
            'Solution': 'Remove unused type declarations from the project.',
        })

    # Rule 5.1
    for line_number, line in enumerate(open(file_path, 'r'), start=1):
        if re.search(r'\bif\s*\(.*\)\s*;', line):
            violations.append({
                'Rule': '5.1',
                'Line': line_number,
                'Detail': 'The if statement shall be followed by a compound statement.',
                'Solution': 'Enclose the code block after the if statement in curly braces to form a compound statement.',
            })

    # Rule 8.4
    for line_number, line in enumerate(open(file_path, 'r'), start=1):
        if re.search(r'\bwhile\s*\(.*\)\s*;', line):
            violations.append({
                'Rule': '8.4',
                'Line': line_number,
                'Detail': 'The while statement shall be followed by a compound statement.',
                'Solution': 'Enclose the code block after the while statement in curly braces to form a compound statement.',
            })

    # Rule 14.4
    for line_number, line in enumerate(open(file_path, 'r'), start=1):
        if re.search(r'\b#define\b.*\\$', line):
            violations.append({
                'Rule': '14.4',
                'Line': line_number,
                'Detail': 'The #define directive shall not be used to hide a macro expansion.',
                'Solution': 'Avoid using the backslash character to split macro definitions across multiple lines.',
            })

    # ... Add more rules as needed ...

    return violations

def export_to_excel(file_path, misra_violations):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Set the column headers
    sheet["A1"] = "Line"
    sheet["B1"] = "MISRA ID"
    sheet["C1"] = "Detail"
    sheet["D1"] = "Solution"

    # Populate the data
    for row, violation in enumerate(misra_violations, start=2):
        sheet[f"A{row}"] = violation["Line"]
        sheet[f"B{row}"] = violation["MISRA ID"]
        sheet[f"C{row}"] = violation["Detail"]
        sheet[f"D{row}"] = violation["Solution"]

    # Save the Excel file
    workbook.save(file_path)

def process_c_files():
    current_folder = os.getcwd()
    files = [f for f in os.listdir(current_folder) if os.path.isfile(f) and f.endswith(".c")]

    misra_check_file = f"misra_check_{datetime.datetime.now().strftime('%Y-%m-%d')}.xlsx"
    workbook = openpyxl.Workbook()

    for file in files:
        misra_violations = detect_misra_violations(file)
        sheet = workbook.create_sheet(title=file)
        export_to_excel(sheet, misra_violations)

    workbook.save(misra_check_file)

process_c_files()