# This code changes the files extensions of the files in all path to csv.

from pathlib import Path

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/GPDirectory")
for path in directory.glob("**/*"): #for path in directory.rglob(*.txt) can also be used.
    if path.is_file():
        newSuffix = ".csv"
        newPath = path.with_name(path.stem + newSuffix)
        path.rename(newPath)

