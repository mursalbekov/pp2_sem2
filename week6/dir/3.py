import os

path = '\Users\tawer\OneDrive\Рабочий стол\pp2\pp2py\week6\builtin'

if os.path.exists(path):
    print('Exists')
    print('File name :', os.path.basename(path))
    print('Dir portion :', os.path.dirname(path))


else: print("Path doesn't exist")