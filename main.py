import os
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import funcs as func

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")
root.minsize(600, 400)
root.resizable(False, False)

def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

root.iconbitmap(resource("assets/images/icon.ico"))

menu = tk.Menu(root)

menu.add_command(label="Save", command=lambda: func.save(workspace=workspace))
menu.add_command(label="Load", command=lambda: func.load(workspace=workspace))
menu.add_command(label="Undo", command=lambda: func.undo(workspace=workspace))
menu.add_command(label="Redo", command=lambda: func.redo(workspace=workspace))
menu.add_command(label="Close File", command=lambda: func.close(workspace=workspace))
menu.add_command(label="Exit Notepad", command=root.quit)

root.configure(menu=menu)

class Editor(ScrolledText):
    file_path = None

workspace = Editor(root, undo=True, maxundo=-1)
workspace.pack(padx=10, pady=10)
workspace.file_path = None

'''
Shortcuts:
Ctrl + S: Save
Ctrl + O: Load
Ctrl + W: Close File
Ctrl + Q: Exit Notepad

Ctrl + Z: Undo
Ctrl + Shift + Z: Redo

Load looks a little different since Tkinter has it's own Ctrl+O shortcut which adds a new line
in this software's "workspace".
'''

root.bind("<Control-s>", lambda event: menu.invoke("Save"))
root.bind("<Control-w>", lambda event: menu.invoke("Close File"))
root.bind("<Control-q>", lambda event: menu.invoke("Exit Notepad"))

workspace.bind("<Control-z>", lambda event: menu.invoke("Undo"))
workspace.bind("<Control-Z>", lambda event: menu.invoke("Redo"))
workspace.bind("<Control-Shift-z>", lambda event: menu.invoke("Redo"))

def load_shortcut(event):
    menu.invoke("Load")
    return "break"

workspace.bind("<Control-o>", load_shortcut)

if __name__ == "__main__":
    root.mainloop()