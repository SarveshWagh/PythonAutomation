# This program adds prefix to all filenames and folders.
from pathlib import Path

pathFiles = Path("allFiles")

for path in pathFiles.iterdir():
    newPathname = path.with_name("new-" + path.stem + path.suffix)
    print(newPathname)
    path.rename(newPathname)
