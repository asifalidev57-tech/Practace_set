import os
path ='example.txt'
if os.path.isfile(path):
    print(f"the path'{path}'is a file ")
elif os.path.isdir(path):
    print(f"the path is'{path}'is directory")
else:
    print(f"the path'{path}'is nor file not directory")

    relative_path="example.txt"
    absolute_path=os.path.abspath(relative_path)
    print(absolute_path)