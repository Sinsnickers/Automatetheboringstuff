#! python3
# backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

import zipfile, os, pathlib

def backupToZip(folder):
    #Backup the complete folder into a zipfile

    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on
    # what files already exist.

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break

        number = number + 1
    
    # TODO: Create the ZIP file.
    print(f"Creating {zipFilename}....")
    backupZip = zipfile.ZipFile(zipFilename,"w")

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {filenames}...")
        #Add the current folder to the zipfile
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
