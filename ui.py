import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class UI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x550")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True)

        dir_container = ttk.LabelFrame(main_container, text="Directory Selection")
        dir_container.pack(fill=tk.X)

        ttk.Label(dir_container, text="Input Directory: ").grid(
            row=0, column=0, sticky=tk.W
        )
        self.input_dir_var = tk.StringVar()
        ttk.Entry(dir_container, textvariable=self.input_dir_var).grid(
            row=0, column=1, sticky=tk.W
        )
        ttk.Button(dir_container, text="Browse", command=self.browse_input_dir).grid(
            row=0, column=2, sticky=tk.W
        )

        ttk.Label(dir_container, text="Output Directory: ").grid(
            row=1, column=0, sticky=tk.W
        )
        self.output_dir_var = tk.StringVar()
        ttk.Entry(dir_container, textvariable=self.output_dir_var).grid(
            row=1, column=1, sticky=tk.W
        )
        ttk.Button(dir_container, text="Browse", command=self.browse_output_dir).grid(
            row=1, column=2, sticky=tk.W
        )

        ext_container = ttk.LabelFrame(main_container, text="Extension: Folder")
        ext_container.pack(fill=tk.BOTH, expand=True)

        tree_view_container = ttk.Frame(ext_container)
        tree_view_container.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(tree_view_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        columns = ("extensions", "folders")

        self.tree = ttk.Treeview(
            tree_view_container,
            columns=columns,
            selectmode="browse",
            show="headings",
            yscrollcommand=scrollbar.set,
        )

        scrollbar.config(command=self.tree.yview)

        self.tree.heading("extensions", text="Extensions")
        self.tree.heading("folders", text="Folders")
        self.tree.column("extensions", width=150)
        self.tree.column("folders", width=250)
        self.tree.pack(fill=tk.BOTH, expand=True)

        controls_container = ttk.Frame(main_container)
        controls_container.pack(fill=tk.X)

        ttk.Label(controls_container, text="Extention: ").grid(row=0, column=0)
        self.ext_entry_text = tk.StringVar()
        ttk.Entry(controls_container, textvariable=self.ext_entry_text).grid(
            row=0, column=1
        )

        ttk.Label(controls_container, text="Folder: ").grid(row=0, column=2)
        self.folder_entry_text = tk.StringVar()
        ttk.Entry(controls_container, textvariable=self.folder_entry_text).grid(
            row=0, column=3
        )

        ttk.Button(
            controls_container, text="add/update", command=self.add_update_row
        ).grid(row=0, column=4)

        ttk.Button(
            controls_container, text="remove", command=self.remove_selected
        ).grid(row=0, column=5)

    def browse_input_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir_var.set(directory)
        return

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_var.set(directory)
        return

    def add_update_row(self):
        ext = self.ext_entry_text.get().strip()
        folder = self.folder_entry_text.get().strip()

        if not ext or not folder:
            messagebox.showwarning(
                "Input Error", "Please provide both extention and folder name"
            )
            return

        found = False

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")

            if values[0] == ext:
                self.tree.item(item, values=(ext, folder))
                found = True
                break

        if not found:
            self.tree.insert("", tk.END, values=(ext, folder))

        self.ext_entry_text = ""
        self.folder_entry_text = ""

        return

    def remove_selected(self):
        selected = self.tree.selection()

        if selected:
            self.tree.delete(selected)
        else:
            messagebox.showwarning("Nothing Selected")


if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()
