import os


#=====================================
#              Input param
#=====================================

Input_txt_name = 'Input_txt.txt'
template_file_name = 'template.txt'

#=====================================
#              Global variables
#=====================================
output_text = ''
cwd = os.getcwd()
print(cwd)
#=====================================
#              Define Function
#=====================================


Input_txt_path = str(cwd) + '\\replace_template\\' + Input_txt_name
template_file_path = str(cwd) + '\\replace_template\\' + template_file_name

# Read file to array
def read_file_to_array(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip the newline character and split by tab
            row = line.strip().split(' ')
            array.append(row)
    return array

#=====================================
#           Main Function
#=====================================



with open(template_file_path, 'r') as template_file:
    template = str(template_file.read())

sheet = read_file_to_array(Input_txt_path)
print(sheet)
print(len(sheet))
print(len(sheet[0]))
for row in range (1,len(sheet)):
    temp = template
    for col in range (len(sheet[0])):
        print('replacing {} with {}'.format(sheet[0][col],sheet[row][col]))

        temp = temp.replace(sheet[0][col], str(sheet[row][col]))
    if row == 1:
        output_text = temp
    else:
        output_text = output_text + "\n" + temp



# Write the modified content to a new text file
with open('output_txt2txt.txt', 'w') as output_file:
    output_file.write(output_text)

print("\nFile created successfully!")