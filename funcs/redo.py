import tkinter as tk

def redo(workspace):
    try:
        workspace.edit_redo()
    except tk.TclError:
        pass  # nothing to redo
    return "break"