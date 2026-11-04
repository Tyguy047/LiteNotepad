import os
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ctypes
from pathlib import Path
import json
import funcs as func

if getattr(sys, "frozen", False):
    app_dir = Path(sys.executable).parent
else:
    app_dir = Path(__file__).parent

config_file = app_dir / "config.json"

if not config_file.exists():
    with open(config_file, "w") as f:
        json.dump({"font_face": "Consolas", "font_size": 11}, f)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Win 8.1+
except Exception:
    pass

root = tk.Tk()

scale = root.winfo_fpixels('1i') / 96

def s(px):
    return int(px * scale)

root.geometry(f"{s(600)}x{s(400)}")
root.minsize(s(600), s(400))
root.title("LiteNotepad")

def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

if sys.platform == "win32":
    root.iconbitmap(default=resource("assets/images/icon.ico"))

else:
    icon = tk.PhotoImage(file=resource("assets/images/icon.png"))
    root.iconphoto(True, icon)
    root._icon = icon

menu = tk.Menu(root)

menu.add_command(label="Save", command=lambda: func.save(workspace=workspace))
menu.add_command(label="Load", command=lambda: func.load(workspace=workspace))
menu.add_command(label="Undo", command=lambda: func.undo(workspace=workspace))
menu.add_command(label="Redo", command=lambda: func.redo(workspace=workspace))
menu.add_command(label="Close File", command=lambda: func.close(workspace=workspace))
menu.add_command(label="Change Font", command=lambda: func.change_font_face(config_file=config_file, workspace=workspace, parent=root))
menu.add_command(label="Change Font Size", command=lambda: func.change_font_size(config_file=config_file, workspace=workspace, parent=root))
menu.add_command(label="Preview HTML/MD", command=lambda: func.render(workspace=workspace, parent=root))
menu.add_command(label="Exit Notepad", command=lambda: func.close_app(workspace=workspace, parent=root))

root.configure(menu=menu)

class Editor(ScrolledText):
    file_path = None
    saved = True

FONT_SIZE = int(func.font_size(config_file=config_file))
FONT_FACE = str(func.font_face(config_file=config_file))

workspace = Editor(root, undo=True, maxundo=-1, font=(FONT_FACE, FONT_SIZE))
workspace.pack(fill="both", expand=True, padx=10, pady=10)
workspace.file_path = None

def on_modified(event):
    if workspace.edit_modified():
        workspace.saved = False
        workspace.edit_modified(False)

workspace.bind("<<Modified>>", on_modified)

'''
Shortcuts:
Ctrl + S: Save
Ctrl + O: Load
Ctrl + W: Close File
Ctrl + Q: Exit Notepad

Ctrl + Z: Undo
Ctrl + Shift + Z: Redo

Ctrl + F: Change Font Face
Ctrl + Shift + F: Change Font Size

Ctrl + R: Preview HTML and/or Markdown

"Load" looks a little different since Tkinter has it's own Ctrl+O shortcut which adds a new line
in this software's "workspace".
'''

root.bind("<Control-s>", lambda event: menu.invoke("Save"))
root.bind("<Control-w>", lambda event: menu.invoke("Close File"))
root.bind("<Control-q>", lambda event: menu.invoke("Exit Notepad"))

workspace.bind("<Control-z>", lambda event: menu.invoke("Undo"))
workspace.bind("<Control-Z>", lambda event: menu.invoke("Redo"))
workspace.bind("<Control-Shift-z>", lambda event: menu.invoke("Redo"))

root.bind("<Control-f>", lambda event: menu.invoke("Change Font"))
root.bind("<Control-Shift-f>", lambda event: menu.invoke("Change Font Size"))
root.bind("<Control-Shift-F>", lambda event: menu.invoke("Change Font Size"))

root.bind("<Control-r>", lambda event: menu.invoke("Preview HTML/MD"))

def load_shortcut(event):
    menu.invoke("Load")
    return "break"

workspace.bind("<Control-o>", load_shortcut)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        root.after(0, lambda: func.load(workspace=workspace, file_path=sys.argv[1]))

    root.protocol("WM_DELETE_WINDOW", lambda: func.close_app(workspace=workspace, parent=root))
    root.mainloop()