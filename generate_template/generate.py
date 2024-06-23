### Generate template file from 2 txt (compare then create)
### Created by PNM3HC

import difflib

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def find_differences(file1_lines, file2_lines):
    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))
    
    common_lines = []
    diff1_lines = []
    diff2_lines = []

    for line in diff:
        if line.startswith('  '):  # No change
            common_lines.append(line[2:])
        elif line.startswith('- '):  # Line in file1 but not in file2
            diff1_lines.append(line[2:])
        elif line.startswith('+ '):  # Line in file2 but not in file1
            diff2_lines.append(line[2:])
    
    return common_lines, diff1_lines, diff2_lines

def create_template(common_lines, diff1_lines, diff2_lines):
    template = []
    keyword_index = 1

    for line in common_lines:
        if line in diff1_lines and line in diff2_lines:
            template.append(f"{{keyword{keyword_index}}}")
            keyword_index += 1
        else:
            template.append(line)
    
    return ''.join(template)

def main():
    file1_lines = read_file('file1.txt')
    file2_lines = read_file('file2.txt')
    
    common_lines, diff1_lines, diff2_lines = find_differences(file1_lines, file2_lines)
    
    template = create_template(common_lines, diff1_lines, diff2_lines)
    
    # Write the modified content to a new text file
    with open('output.txt', 'w') as output_file:
        output_file.write(template)
    print("\nFile created successfully !!!\n")

if __name__ == "__main__":
    main()