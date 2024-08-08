import os
import subprocess
import pylint.lint

# Get the current directory
current_dir = os.getcwd()

# Get all C files in the current directory
c_files = [file for file in os.listdir(current_dir) if file.endswith('.c')]

# Iterate over the C files and check MISRA compliance
for c_file in c_files:
    # Run Pylint with the MISRA 2012 ruleset
    result = subprocess.run(['pylint', '--disable=all', '--enable=pylint.extensions.misrac2012', c_file], capture_output=True, text=True)
    print(result)

    # Write the output to a file
    output_file = os.path.splitext(c_file)[0] + '_misra_output.txt'
    with open(output_file, 'w') as f:
        f.write(result.stdout)

    print(f"MISRA Compliance report for {c_file} saved to {output_file}")