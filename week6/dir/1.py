import os
path = '\Users\tawer\OneDrive\Рабочий стол\pp2\pp2py\week6\builtin'

for i in os.listdir(path):     # only directories
    if os.path.isdir(os.path.join(path, i)): print(i, end='   ')
print()
for i in os.listdir(path):      # only files
    if not os.path.isdir(os.path.join(path, i)): print(i, end= '    ')
print()

print(os.listdir(path))  # all directories, files

