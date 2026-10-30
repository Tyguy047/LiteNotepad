import os
import tkinter as tk
from tkinter import filedialog, messagebox
from binaryornot.helpers import is_binary_string

def load(workspace, file_path=None):
    if file_path is None:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = filedialog.askopenfilename(
            title="Select a file to edit",
            initialdir=desktop
        )

    if not file_path:
        return

    with open(file_path, "rb") as f:
        binary = is_binary_string(f.read(512))

        if binary:
            tk.messagebox.showerror("Error", "File does not contain any editable text!")
            return

    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()

    except UnicodeDecodeError:
        messagebox.showerror("Error", "File isn't UTF-8 text.")
        return

    workspace.delete("1.0", "end")
    workspace.insert("1.0", content)
    workspace.file_path = file_path
    workspace.saved = True
    workspace.edit_modified(False)
    return