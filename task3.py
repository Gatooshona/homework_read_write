import os
from pprint import pprint


current = os.getcwd()
folder = 'task3-text'
target_folder = os.path.join(current, folder)

files = os.listdir(target_folder)
files_map = {}
for file in files:
    file_path = os.path.join(target_folder, file)
    f = open(file_path, 'r', encoding='utf-8')
    res = f.readlines()
    len_f = len(res)
    files_map[len_f] = {
        'name': file,
        'text': res
    }
    f.close()

sorted_files_map = sorted(files_map.items())

for element in sorted_files_map:
    write_f = open('4.txt', 'a', encoding='utf-8')
    write_f.write(element[1]['name'])
    write_f.write('\n')
    write_f.write(str(element[0]))
    write_f.write('\n')
    write_f.writelines(element[1]['text'])
    write_f.write('\n')
    write_f.write('\n')
    write_f.close()
