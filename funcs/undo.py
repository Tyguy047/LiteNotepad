import tkinter as tk

def undo(workspace):
    try:
        workspace.edit_undo()
    except tk.TclError:
        pass  # nothing to undo
    return "break"