from sys import argv, exit
import os
import shutil

# checks if the number of cmd ln args is not correct
if len(argv) != 3:
    print("Usage: Python script input_dir output_dir")
    exit(1)

input_dir = argv[1]
output_dir = argv[2]

# checks if the input_dir is not a dir
if not os.path.isdir(input_dir):
    print("Invalid input dir")
    exit(2)
# checks if the output_dir is not a dir
if not os.path.isdir(output_dir):
    os.mkdir(argv[2])

type2ext = {
    "Image": ['.jpg', '.jpeg', '.bmp', '.png'],
    "Video": ['.mp4', '.avi', '.mov', '.mkv'],
    "Code":  ['.html', '.htm', '.css', '.c', '.cpp', '.js', '.ts', '.py'],
    "Document": ['.csv', '.txt'],
}

ext2type = {}

# ext is stored as key and type as value for easier and faster lookups
for key in type2ext:
    value = type2ext[key]
    for ext in value:
        ext2type[ext] = key

CURRENT_SCRIPT = os.path.basename(__file__)

files_to_move = 0
files_moved = 0

# loops over every item in the input_dir
for filename in os.listdir(input_dir):
    # if filename is dir or the current_script, skip this iteration
    if os.path.isdir(filename) or filename == CURRENT_SCRIPT:
        continue

    # store the extension of filename
    name, extension = os.path.splitext(filename)
    # target_dir is the dir name in which the current file destined to go
    target_dir = ext2type.get(extension)

    if target_dir is None:
        target_dir = "Others"
    
    abs_target_dir = os.path.join(output_dir, target_dir)

    # if the target dir not exists in the output_dir then mkdir 
    if not os.path.isdir(abs_target_dir):
        os.mkdir(abs_target_dir)

    destination_path = os.path.join(abs_target_dir, filename)
    # omit the /filename from the destination_path
    head_dst_path, _ = os.path.split(destination_path)
    n = 1
    # while the destination_path exists
    # (there is already a file named filename in the destination folder)
    # change the destination_path to ../filename(n).xyz
    while os.path.exists(destination_path):
        # name = name(n) where n is the number of files with the same name - 1
        name = name + '(' + str(n) + ')'
        new_filename = name + extension
        destination_path = os.path.join(head_dst_path, new_filename)
        n += 1
    
    # abs path of the filename
    filepath = os.path.join(os.path.abspath(input_dir), filename)
    files_to_move += 1

    try:
        shutil.move(filepath, destination_path)
        print(f"{filename} => \n{destination_path}")
        files_moved += 1
    except FileNotFoundError:
        print("Source file not found")
    except PermissionError:
        print("Permission denied. Unable to move the file.")
    except Exception as e:
        print(f"Error: {e}")

print()
print(f"{files_moved} / {files_to_move} files were moved successfully")