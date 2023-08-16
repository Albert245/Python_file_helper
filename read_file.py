import os
import time

start_time = time.time()
cwd = os.getcwd()
a2l=''

def file_Dir(dir,keyname):
    fileNames = os.listdir(dir)
    file_name = ''
    for fileName in fileNames:
        if(keyname in fileName):
            # file_path = format(os.path.join(dir, fileName))
            file_name = fileName
    return file_name

def read_file(file_name):
    data  = open(file_name,'r').read()
    return data

# def find_paragraph(data, keyname, type_parg):
    

with open('test.txt','w') as f:
    a2l = file_Dir(cwd,'.a2l')
    f.write(a2l+'\n')
    f.write('current_Dir:'+cwd)
    data = read_file(a2l)
    end_time = time.time()
    f.write('\nExecution time: '+str(end_time-start_time)+' s')