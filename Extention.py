import shutil
import os

destination = "D:\Recovered\ZIP"
s = "D:\\"
source = os.listdir(s)
i = 0
for files in source:
    if files.endswith(".zip"):
        scr = os.path.join(s, files)
        shutil.move(scr, destination)
        print("moving {}".format(scr))
        i = i+1
print("{} files moved".format(i))

