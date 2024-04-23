file_path = 'hexfile.txt'
a = ''
for i in range(0,65536):
    b = hex(i)
    b = '0'*(6-len(b))+str(b[2:])
    a = a  + '22 ' + str(b) + '\n' +'SLEEP 1000' + '\n'
with open(file_path, "w") as file:
    file.write(a)