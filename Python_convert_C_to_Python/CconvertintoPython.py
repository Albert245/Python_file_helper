import re

def convert_c_to_python(c_code):
    # Remove preprocessor directives
    c_code = re.sub(r'#\s*include\s*<.*?>', '', c_code)
    c_code = re.sub(r'#\s*include\s*".*?"', '', c_code)
    c_code = re.sub(r'#\s*define\s+\w+\s+\w+', '', c_code)
    
    # Convert data types
    c_code = re.sub(r'\bint\b', 'int', c_code)
    c_code = re.sub(r'\bfloat\b', 'float', c_code)
    c_code = re.sub(r'\bdouble\b', 'float', c_code)
    c_code = re.sub(r'\bchar\b', 'str', c_code)
    
    # Convert control structures
    c_code = re.sub(r'\bfor\s*\((.*?);(.*?);(.*?)\)', 'for \\1 in range(\\2, \\3):', c_code)
    c_code = re.sub(r'\bwhile\s*\((.*?)\)', 'while \\1:', c_code)
    c_code = re.sub(r'\bdo\s*{', 'while True:', c_code)
    c_code = re.sub(r'\bif\s*\((.*?)\)', 'if \\1:', c_code)
    c_code = re.sub(r'\belse\s*{', 'else:', c_code)
    c_code = re.sub(r'\belse\s+if\s*\((.*?)\)', 'elif \\1:', c_code)
    
    # Convert function definitions
    c_code = re.sub(r'\bvoid\b', 'def', c_code)
    c_code = re.sub(r'\bint\b', 'int', c_code)
    c_code = re.sub(r'\bfloat\b', 'float', c_code)
    c_code = re.sub(r'\bdouble\b', 'float', c_code)
    c_code = re.sub(r'\bchar\b', 'str', c_code)
    
    # Convert function calls
    c_code = re.sub(r'\bprintf\s*\((.*?)\)', 'print(\\1)', c_code)
    c_code = re.sub(r'\bscanf\s*\((.*?)\)', '\\1 = input()', c_code)
    
    return c_code

# Read C script from file
with open('input.c', 'r') as file:
    c_code = file.read()

# Convert C script to Python
python_code = convert_c_to_python(c_code)

# Write Python script to file
with open('output.py', 'w') as file:
    file.write(python_code)
