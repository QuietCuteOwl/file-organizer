import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from file_organizer import DEFAULT_type2ext


class UI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("700x600")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Basic Styling
        # Using a consistent font (Segoe UI) and background color (#f0f0f0).
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10))
        self.style.configure("TEntry", font=("Segoe UI", 10))
        self.style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
        self.style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()
        self.show_default_data()

    def create_widgets(self):
        # Main Container
        main_container = ttk.Frame(self.root, padding="20 20 20 20")
        main_container.pack(fill=tk.BOTH, expand=True)
        # Directory Conatiner
        dir_container = ttk.LabelFrame(
            main_container, text="Directory Selection", padding="10 10 10 10"
        )
        dir_container.pack(fill=tk.X, pady=(0, 15))
        # Tell tkinter to expand entry when window resized
        dir_container.columnconfigure(1, weight=1)
        # Input Directory
        ttk.Label(dir_container, text="Input Directory:").grid(
            row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5
        )
        self.input_dir_var = tk.StringVar()
        # sticky=tk.EW makes the entry stretch from East to West
        ttk.Entry(dir_container, textvariable=self.input_dir_var).grid(
            row=0, column=1, sticky=tk.EW, padx=5, pady=5
        )
        ttk.Button(dir_container, text="Browse", command=self.browse_input_dir).grid(
            row=0, column=2, sticky=tk.W, padx=(5, 0), pady=5
        )
        # Output Directory
        ttk.Label(dir_container, text="Output Directory:").grid(
            row=1, column=0, sticky=tk.W, padx=(0, 5), pady=5
        )
        self.output_dir_var = tk.StringVar()
        ttk.Entry(dir_container, textvariable=self.output_dir_var).grid(
            row=1, column=1, sticky=tk.EW, padx=5, pady=5
        )
        ttk.Button(dir_container, text="Browse", command=self.browse_output_dir).grid(
            row=1, column=2, sticky=tk.W, padx=(5, 0), pady=5
        )
        # Extension Container
        ext_container = ttk.LabelFrame(
            main_container, text="Extension Mapping", padding="10 10 10 10"
        )
        ext_container.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        # Container specifically for the Treeview and Scrollbar
        tree_view_container = ttk.Frame(ext_container)
        tree_view_container.pack(fill=tk.BOTH, expand=True)
        # Scrollbar Configuration
        # Creating scrollbar first and pack it before treeview
        # otherwise treeview will take the entire space and scroll bar will move to the bottom
        scrollbar = ttk.Scrollbar(tree_view_container, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Treeview Configuration
        columns = ("extensions", "folders")
        self.tree = ttk.Treeview(
            tree_view_container,
            columns=columns,
            selectmode="browse",
            show="headings",  # 'headings' hides the default empty tree column
            yscrollcommand=scrollbar.set,  # Link the tree's vertical scroll to the scrollbar
        )

        # Link the scrollbar's movement to the tree's yview
        scrollbar.config(command=self.tree.yview)

        self.tree.heading("extensions", text="Extensions (e.g., .jpg, .png)")
        self.tree.heading("folders", text="Target Folder")
        self.tree.column("extensions", width=200, anchor=tk.W)
        self.tree.column("folders", width=300, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True)
        # Controls Container
        controls_container = ttk.Frame(main_container)
        controls_container.pack(fill=tk.X)

        # Configure Grid Layout for Controls
        controls_container.columnconfigure(1, weight=1)
        controls_container.columnconfigure(3, weight=1)
        # Extension Entry
        ttk.Label(controls_container, text="Extension:").grid(
            row=0, column=0, padx=(0, 5), sticky=tk.W
        )
        self.ext_entry_text = tk.StringVar()
        ttk.Entry(controls_container, textvariable=self.ext_entry_text).grid(
            row=0, column=1, sticky=tk.EW, padx=5
        )
        # Folder Entry
        ttk.Label(controls_container, text="Folder:").grid(
            row=0, column=2, padx=5, sticky=tk.W
        )
        self.folder_entry_text = tk.StringVar()
        ttk.Entry(controls_container, textvariable=self.folder_entry_text).grid(
            row=0, column=3, sticky=tk.EW, padx=5
        )
        # Button Container
        btn_frame = ttk.Frame(controls_container)
        btn_frame.grid(row=0, column=4, columnspan=2, padx=(10, 0))

        ttk.Button(btn_frame, text="Add/Update", command=self.add_update_row).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(btn_frame, text="Remove", command=self.remove_selected).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(btn_frame, text="Organize", command=self.init_organizer).pack(
            side=tk.LEFT, padx=5
        )

    def show_default_data(self):
        for type in DEFAULT_type2ext:
            for ext in DEFAULT_type2ext[type]:
                self.tree.insert("", tk.END, values=(ext, type))
        
        return

    def browse_input_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir_var.set(directory)

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_var.set(directory)

    def add_update_row(self):
        ext = self.ext_entry_text.get().strip()
        folder = self.folder_entry_text.get().strip()

        if not ext or not folder:
            messagebox.showwarning(
                "Input Error", "Please provide both extension and folder name"
            )
            return

        # Ensure extension starts with dot if user forgot
        if not ext.startswith("."):
            ext = "." + ext

        found = False
        # Check if extension already exists in the tree to update it
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values[0] == ext:
                self.tree.item(item, values=(ext, folder))
                
                found = True
                break
        # If not found, insert a new row
        if not found:
            self.tree.insert("", tk.END, values=(ext, folder))

        self.update_default(ext=ext, type=folder)

        # Clear the entry fields
        self.ext_entry_text.set("")
        self.folder_entry_text.set("")

    def remove_selected(self):
        selected = self.tree.selection()
        if selected:
            ext, type = self.tree.item(selected[0], "values")
            self.tree.delete(selected)
            self.remove_default(ext=ext, type=type)
        else:
            messagebox.showwarning("Selection Error", "Please select an item to remove")

    def init_organizer(self):
        from file_organizer import organizer

        organizer(input_dir=self.input_dir_var.get(), output_dir=self.output_dir_var.get())

        return
    

    def update_default(self, ext, type):
        values: list = DEFAULT_type2ext[type]
        if values:
            DEFAULT_type2ext[type].append(ext)
        else:
            DEFAULT_type2ext[type] = ext


    def remove_default(self, ext, type):
        try:
            DEFAULT_type2ext[type].remove(ext)
        except ValueError:
            return

if __name__ == "__main__":
    root = tk.Tk()
    # Set a minimum size to prevent the UI from being squashed too small
    root.minsize(600, 500)
    app = UI(root)
    root.mainloop()