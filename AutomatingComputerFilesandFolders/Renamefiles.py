# This program renames all filenames based on folders it is stored in.
from pathlib import Path

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/testDir")


for items in directory.glob("**/*"): # This technique iterates through all the directories and files, entire tree.
    if items.is_file():
        month = items.parts[-2] # items.parts functionality fragments the entire dir into a tuple.
        newItem = items.with_name(month + "-" + items.name)
        items.rename(newItem)
