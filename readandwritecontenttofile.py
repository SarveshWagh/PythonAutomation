from pathlib import Path

p1 = Path("files/file4.txt")
if p1.exists():
    with open(p1, "r") as file:
        print(file.read())

else:
    with open(p1, "w") as file:
        file.write("Adding sample content to the new file, 'file4'.")


print("Testing git changes!!")
