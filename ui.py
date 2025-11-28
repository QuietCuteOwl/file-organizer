# create main_container
# pack it
# create container for directory selection inside main_container
# pack it (expand x)
#  Inside dir_container
## Input dir label on the left
## Input_dir entry in the middle
## Input_dir browse button (connected to a tk.String() textvar)
## below input dir
## Output_dir label on the left
## Output_dir entry in the middle
## Output_dir browse button (connected to a tk.String() textvar)
# create extension_management container (LabelFrame)
# pack it
# Inside extension_management container
## Create a tree_view container
## pack it
## Inside tree_view container
### Create a tree_view with columns(extensions, folders), mode browse
### Inside tree_view
#### set heading, width of column, and pack the tree_view
### add a scrollbar (as scrollbar) inside tree_view container, cmd=self.tree.yview (to connect it to the tree_view)
### pack the scrollbar
### link the tree back to the scrollbar with
#### self.tree.configure(yscrollcommand=scrollbar.set)
# create controls_container
# pack it
# Inside controls_container
## Label named extension @ grid(0, 0)
## Entry for extension @ grid(0, 1)
## Label named Folder type @ grid(0, 2)
## Entry for Folder type @ grid(0, 3)
## add/update button to add/update a pair @ 0, 4
## remove button to remove the selected pair @ 0, 5

# A func to browse_input_dir connected to input_browse btn
## directory = filedialog.askdirectory() # to open file manager
## if directory (if user selected a path)
## set the input_entry's content to the selected directory's path via the tk.StringVar()
# Do the same as above for output_browse btn aswell
#
# A func to add/update the tree_view
## get the ext from the ext entry and folder from folder entry
## first check if both of them are filled
## if not then messagebox.error them
## set a var found = false
## for item in self.tree.get_children()
## self.tree (tree_view), .get_children() (returns a unique id of every row)
### values = self.tree.item(item, "values")
### .item(id, data), id is the row id, data is what data is requested from that row
### if the values[0] (the ext for a row) == extension (entered by user):
#### update that row with the given extension and folder_type
#### found = true and break
##
## if not found:
### insert the given data into the tree
##
## clear both entries to take new values
##
#
# a func for when remove btn is clicked
## get the selected row by self.tree.selection()
## if there is something selected
### delete that row
## else
### show warning via errorbox
