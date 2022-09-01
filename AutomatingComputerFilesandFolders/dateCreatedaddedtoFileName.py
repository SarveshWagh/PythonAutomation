from pathlib import Path
from datetime import datetime

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/GPDirectory")
for path in directory.glob("**/*"): # Iterates or walks through all the folders, subfolders tile the files.
    if path.is_file(): # Checking if the iterable is a file
        stats = path.stat() # This functionality extracts all the stats related to the path
        seconds_created = stats.st_ctime # st_ctime is create time [in seconds] of the file, so extracting oly create time from all stats.
        date_created = datetime.fromtimestamp(seconds_created) # Converting the seconds to date and time in date type.
        date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S") # Converting date type to String.
        newFilename = path.with_name(date_created_str + "_" + path.name) # Creating new filename
        path.rename(newFilename) # Renaming old pathnames to new pathnames where the files names get altered.

