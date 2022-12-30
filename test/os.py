import os

source_dir = "C:/Users/Sergio/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        entryName = entry.name.split(".")
        # print(entryName)
        print(entryName[-1])
