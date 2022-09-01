from pathlib import Path

p1 = Path("Testing/file3.txt")

print(p1) # Prints the entire path dir/subdir/filename
print(p1.name) # Prints the filename ONLY
print(p1.stem) # Prints the prefix of the filename
print(p1.suffix) # Prints the suffix/type of the filename

with open(p1, "r") as file:
    print(file.read())

filePaths = Path("Testing")
for item in filePaths.iterdir():
    print(item)


