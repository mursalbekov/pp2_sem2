

import os

path = '\Users\tawer\OneDrive\Рабочий стол\pp2\pp2py\week6\builtin\file-dir\A.txt'

if os.path.exists(path):
    os.remove(path)
else: print('Path does not exist')