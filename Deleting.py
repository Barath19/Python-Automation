import os

dir_name = "D:\\"
test = os.listdir(dir_name)
j = 0
for item in test:
    if item.endswith(".cab") or item.endswith(".xz"):
        os.remove(os.path.join(dir_name, item))
        print("Removing {}".format(item))
        j = j+1

print("{} removed".format(j))
