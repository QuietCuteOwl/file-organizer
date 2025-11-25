
# take cmd line input for input dir and output dir
# validate cmd line args
## if the input dir doesn't exist, let the user know and exit
## if the output dir doesn't exist, create one in the path this program is running

# in a dict
## store file extensions as value and file type as key
### for eg: "Image": ['.jpg', '.bmp', '.etc']

# create a new dict and store the file extensions as key (from the previous dict) &&
# the file types as value (from the previous dict)
# for a faster and easier lookup

# in the input dir, loop over every file/dir as filename
## if filename is a dir or filename is __file__
### go to the next iteration
## seperate the name and the extension of file
### store the extension in a var
## empty var target_dir
## index into the dict with the extension as the key
### if the key doesn't correspond to a value
#### target_dir = "Others"
### else
#### target_dir = "{value}"
## if the target_dir not exists in the output_dir
### create target_dir in output_dir
## target_path = abspath(target_dir) + lastpart(filename)
## n = 1
## while the target_path exists
### filename = name_part(filename) + str(n) + extension_part(filename)
### target_path = abspath(target_dir) + filename
## move filename from where it is to target_path
# end