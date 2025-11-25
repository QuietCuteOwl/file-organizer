import os
from sys import argv, exit

if len(argv) != 2:
    print("Usage: Python script dir")
    exit(1)

type2ext = {
    "Image": ['.jpg', '.jpeg', '.bmp', '.png'],
    "Video": ['.mp4', '.avi', '.mov', '.mkv'],
    "Code":  ['.html', '.htm', '.css', '.c', '.cpp', '.js', '.ts', '.py'],
    "Document": ['.csv', '.txt'],
    "Others": ['.xyz', '.idk'],
}

ext2type = {}

# ext is stored as key and type as value for easier and faster lookups
for key in type2ext.keys:
    value = type2ext[key]
    for ext in value:
        ext2type[ext] = key

name = "test_"
target_dir = os.abs(argv[1])

for key in ext2type.keys:
    filename = name + ext2type[key] + key
    destination = os.path.join(target_dir, filename)
    if os.path.exists(destination):
        continue
    with open(destination, "w") as f:
        f.write("Test script")

print("Created test files")
