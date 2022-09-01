# This program renames all filenames based on folders and subfolders it is stored in. Year-month-oldfilename
from pathlib import Path

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/GPDirectory")

for path in directory.glob("**/*"): # This functionality iterates through all the folders, subfolders and files from the Path instance created above.
    if path.is_file():
        month = path.parts[-2] # This functionality fragments all path into tuples. Each tupe will have values of the directory structure.
        year = path.parts[-3]
        newFilename = path.with_name(year + "-" + month + "-" + path.name) # Here, we are creating new pathnames.
        path.rename(newFilename) # Here we are renaming the old paths with new path created above.
