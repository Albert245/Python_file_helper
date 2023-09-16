import os
import subprocess

# Path to your C program or directory containing C files
c_path = '/path/to/your/c_program.c'  # or '/path/to/your/c_directory'

# Function name to check coverage (set to None to check coverage for all functions)
function_name = 'your_function_name'  # or None

# Build the C program or compile all C files in the directory
if os.path.isfile(c_path):
    subprocess.run(['gcc', '-fprofile-arcs', '-ftest-coverage', c_path, '-o', 'c_program'])
else:
    subprocess.run(['gcc', '-fprofile-arcs', '-ftest-coverage', '-g', '-O0', '-c', c_path + '/*.c'])
    subprocess.run(['gcc', '-fprofile-arcs', '-ftest-coverage', '-g', '-o', 'c_program', c_path + '/*.o'])

# Run the C program with coverage
subprocess.run(['./c_program'])

# Generate coverage report for each function or all functions
if function_name:
    subprocess.run(['gcovr', '-r', '.', '-f', function_name])
else:
    subprocess.run(['gcovr', '-r', '.'])

# Clean up generated files
os.remove('c_program')