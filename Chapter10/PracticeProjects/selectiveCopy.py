#! python3
# selectiveCopy.py - searches a folder tree for specific 
# file extensions

import os,shutil
from pathlib import Path

os.chdir("c:\\users\\bero8\\documents")
currentFolder = Path.cwd()
if  Path(f"{currentFolder}\\backup").exists():
    backupFolder = Path(f"{currentFolder}\\backup")
else:
    backupFolder = Path(f"{currentFolder}\\backup").mkdir()

filenames = list(currentFolder.glob("*.ods"))
for filename in filenames:
    print(filename)
    shutil.copy(filename,backupFolder)