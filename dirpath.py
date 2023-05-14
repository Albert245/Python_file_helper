import openpyxl
import os
import time

start_time = time.time()
cwd = os.getcwd()
support_file='1'

def listDir(dir,keyname):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if(keyname in fileName):
            file_path = format(os.path.join(dir, fileName))
            file_name = fileName
    return file_path,file_name


with open('test1.txt','w') as f:
    support_file,sp = listDir(cwd,'Support')
    f.write(support_file+'\n')
    f.write('current_Dir:'+cwd)
    end_time = time.time()
    f.write('\nExecution time: '+str(end_time-start_time)+' s')