# This code creates empty files in any particular directory instance.

from pathlib import Path

directory = Path("/Users/sarvesh.wagh/Desktop/PythonAutomation/GPDirectory/2021/Jan")

for i in range(1, 11):
    fileName = str(i) + ".txt"
    newFile = directory/Path(fileName) # Joining the existing directory instance to the new file that's created using for loop.
    newFile.touch() # Touch method tp create new files.
