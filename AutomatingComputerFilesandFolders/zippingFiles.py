# This code is written to zip or archive any number of text files.

from pathlib import Path
import zipfile #zipfile library

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/AutomatingComputerFilesandFolders")
archiveDir = directory / Path("archives.zip") # This is the path where the archives has to be stored.

with zipfile.ZipFile(archiveDir, 'w') as zf: #from the zipfile library, ZipFile class instance, zf is created and archive dir passed in write mode.
    for file in directory.rglob("*.txt"): # Iterating through all text files which has to be zipped in the directory.
        zf.write(file) #Using the ZipFile instance to zip the text files.

