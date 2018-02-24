import shutil
import os

destination = "D:\\"

for num in range(44, 171):
    s = "D:\\recup_dir."
    so = s + str(num)
    source = os.listdir(so)

    for files in source:
        scr = os.path.join(so, files)
        shutil.move(scr, destination)

    print(so)
    print(" done ")
