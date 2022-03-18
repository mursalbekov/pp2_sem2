import os

path  = os.getcwd()

if os.access(path, os.F_OK): print('Exist')
if os.access(path, os.R_OK): print('Readable')
if os.access(path, os.W_OK): print('Writable')
if os.access(path, os.X_OK): print('Executable')