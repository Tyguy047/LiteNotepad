import os
import tkinter as tk
from tkinter import messagebox, filedialog

def save(workspace):
    path = workspace.file_path
    content = workspace.get("1.0", "end-1c")

    if not path:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        path = filedialog.asksaveasfilename(
            title="Save file",
            defaultextension=".txt",
            initialdir=desktop
        )

        if not path:
            tk.messagebox.showinfo("Save", "File save cancelled.")
            return
        workspace.file_path = path

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    tk.messagebox.showinfo("Save", "File saved successfully!")
    return