import os
from sys import argv, exit

if len(argv) != 2:
    print("Usage: Python script dir")
    exit(1)

input_dir = argv[1]

if not os.path.exists(input_dir):
    print(f"{input_dir} does not exists")
    exit(2)
elif not os.path.isdir(input_dir):
    print(f"{input_dir} is not a directory")
    exit(3)


type2ext = {
    "Image": ['.jpg', '.jpeg', '.bmp', '.png'],
    "Video": ['.mp4', '.avi', '.mov', '.mkv'],
    "Code":  ['.html', '.htm', '.css', '.c', '.cpp', '.js', '.ts', '.py'],
    "Document": ['.csv', '.txt'],
    "Others": ['.xyz', '.idk'],
}

ext2type = {}

# ext is stored as key and type as value for easier and faster lookups
for key in type2ext:
    value = type2ext[key]
    for ext in value:
        ext2type[ext] = key

name = "test_"
target_dir = os.path.abspath(input_dir)

for key in ext2type:
    # for eg: test_ + {value} + key = test_Image.jpg
    filename = name + ext2type[key] + key
    destination = os.path.join(target_dir, filename)
    # if destination already exists
    if os.path.exists(destination):
        n = 1
        name, extension = os.path.splitext(filename)
        head_dst, _ = os.path.split(destination)
        # while the destination exists
        # (there is already a file named filename in the destination folder)
        # change the destination to ../filename(n).xyz
        while os.path.exists(destination):
            # name = name(n) where n is the number of files with the same name - 1
            name = name + '(' + str(n) + ')'
            new_filename = name + extension
            destination = os.path.join(head_dst, new_filename)
            n += 1
    # open file as f in write mode
    with open(destination, "w") as f:
        f.write("Test script")

print("Created test files")
