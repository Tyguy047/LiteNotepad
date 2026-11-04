import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def save(workspace):
    path = workspace.file_path
    content = workspace.get("1.0", "end-1c")

    if not path:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        path = filedialog.asksaveasfilename(
            title="Save file",
            initialdir=desktop,
            defaultextension=".txt" if sys.platform == "win32" else "",
            filetypes=[
                ("Text File", "*.txt"),
                ("All Files", "*.*"),
                ("Python", "*.py"),
                ("C", "*.c"),
                ("C Header", "*.h"),
                ("C++", "*.cpp"),
                ("C++ Header", "*.hpp"),
                ("C#", "*.cs"),
                ("Java", "*.java"),
                ("JavaScript", "*.js"),
                ("TypeScript", "*.ts"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
                ("PHP", "*.php"),
                ("Ruby", "*.rb"),
                ("Go", "*.go"),
                ("Rust", "*.rs"),
                ("Swift", "*.swift"),
                ("Kotlin", "*.kt"),
                ("Lua", "*.lua"),
                ("SQL", "*.sql"),
                ("Batch File", "*.bat"),
                ("PowerShell", "*.ps1"),
                ("Shell Script", "*.sh"),
                ("JSON", "*.json"),
                ("XML", "*.xml"),
                ("YAML", "*.yaml"),
                ("TOML", "*.toml"),
                ("INI", "*.ini"),
                ("CSV", "*.csv"),
                ("Markdown", "*.md"),
                ("Log File", "*.log"),
                ("Inno Setup Script", "*.iss")
            ]
        )

        if not path:
            tk.messagebox.showinfo("Save", "File save cancelled.")
            return
        workspace.file_path = path

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    workspace.saved = True
    tk.messagebox.showinfo("Save", "File saved successfully!")
    return