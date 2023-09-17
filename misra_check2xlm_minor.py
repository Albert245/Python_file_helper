import openpyxl
import re

def detect_misra_violations(file_path):
    # Regular expressions for MISRA 2012 patterns
    misra_patterns = {
        "Rule 1.1": r"//[^\n]*",
        "Rule 2.2": r"if\s*\(\s*0\s*\)",
        # Add more MISRA patterns here
    }

    misra_violations = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        for misra_id, pattern in misra_patterns.items():
            if re.search(pattern, line):
                misra_violations.append({
                    "Line": line_number,
                    "MISRA ID": misra_id,
                    "Detail": "MISRA 2012 violation detected",
                    "Solution": "Provide appropriate solution for MISRA violation",
                })

    return misra_violations

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

    # Set the sheet name as the file name
    sheet.title = file_path.split("/")[-1]

    # Save the Excel file
    workbook.save(f"{file_path}.xlsx")

# Provide the path to your .c file
c_file_path = "G:/Side_Project/Nhat_bitloss_tool/pro.c"

# Detect MISRA violations
violations = detect_misra_violations(c_file_path)

# Export to Excel
export_to_excel(c_file_path, violations)