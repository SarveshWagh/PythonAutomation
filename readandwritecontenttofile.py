from pathlib import Path

p1 = Path("file2.txt")
if p1.exists():
    with open(p1, "r") as file:
        print(file.read())

else:
    with open(p1, "w") as file:
        file.write("Adding sample content to the new file, 'file2'.")
