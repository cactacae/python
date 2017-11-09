
import os

path = os.get_exec_path(env=None)

print("Search Path")
print(path)
print("Current directory : " + os.getcwd())

files = os.popen('ls *.*')
for file in files:
    print(file, end='')
