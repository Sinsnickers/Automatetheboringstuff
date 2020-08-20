#! python3
#! deletingFiles - searches for big files of size
# the user defines and print it to the screen

import os
from pathlib import Path
os.chdir("C:\\ProgramData")
searchFolder = Path.cwd()
number = 0
for folder, subfolders, filenames in os.walk(searchFolder):
    for subfolder in subfolders:
        for filename in filenames:
            fileSize = os.path.getsize(os.path.abspath(os.path.join(folder, filename)))
            if fileSize > 3000000:
                print(f"{fileSize} {os.path.abspath(os.path.join(folder, filename))}")
        