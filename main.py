import os
import shutil


dir = "C:/Users/mahdi/Desktop/n"
dir_list = os.listdir(dir)
print("Files and directories in '", dir, "' :")
# prints all files
print(dir_list)
folders = []
for file in dir_list:
    ft = os.path.splitext(file)
    folders.append(ft[1])

folders = set(folders)
print(folders)
for i in folders:
    newfol = os.path.join(dir,i)
    if not os.path.exists(newfol):
        os.mkdir(newfol)

            
for file in dir_list:
    #print(dir+ '/'+file)
    if not os.path.isdir(dir+ '/' + file):
        fld = os.path.splitext(file)[1]
        if not os.path.exists(fld):
            print(f'{file} goes to {fld}')
            shutil.move(dir+ '/' + file, dir + '/' + fld)
        else:
            print(f'there is no place for {file}')
