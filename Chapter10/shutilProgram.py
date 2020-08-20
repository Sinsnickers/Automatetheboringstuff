import shutil, os, zipfile
from pathlib import Path
import send2trash

p = Path.home()
#os.mkdir("someFolder")
#shutil.copy(p / 'spam.txt', p / 'someFolder') # copy the file into a folder
#shutil.copy(p / 'eggs.txt', p / 'someFolder/eggs2.txt') # copy the file into a folder and renames it in the folder
#shutil.copytree(p / "someFolder", p / "someFolder_backup") # copy the folder to new folder or backup
#shutil.move("c:\\users\\bero8\\bacon.txt","c:\\users\\bero8\\eggs") # moves the file to new folder, if folder doesnt exist, the file is renamed
#for filename in Path.home().glob("*.rxt"):   # very unsafe way to delete files, cause it ignores the bin
    #os.unlink(filename)
    #print(filename)

#baconFile = open("bacon.txt","a")      # safe way to delete files, cause they will be send to the bin
#baconFile.write("Bacon is not a vegetable")
#baconFile.close()
#send2trash.send2trash("bacon.txt")

#for folderName, subfolders, filenames in os.walk("c:\\users\\bero8\\someFolder"): #walk the whole foldertree till its end
    #print(f"The current folder is named {folderName}")

    #for subfolder in subfolders:
    #    print(f"The subfolder is named {subfolder}")

    #for filename in filenames:
    #    print(f"The file is named {filename}")

    #print("")

#exampleZip = zipfile.ZipFile(p / "example.zip")
#exampleZip.namelist() #tells you the names in the zipfile
#print(exampleZip.namelist()) 
#spamInfo = exampleZip.getinfo("spam.txt")
#print(spamInfo.file_size)
#print(spamInfo.compress_size)
#print("Compressed file is " + str(round(spamInfo.file_size/spamInfo.compress_size,2)) + "-times smaller")
#exampleZip.close()

#exampleZip = zipfile.ZipFile(p / "example.zip") #extracts zipfile into the current workingfolder
#exampleZip.extractall()
#exampleZip.close()

#os.chdir(p)
#newZip =zipfile.ZipFile(p / "newZip.zip","w")
#newZip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()



