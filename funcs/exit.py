from tkinter import messagebox

def close_app(workspace, parent):
    if not workspace.saved:
        answer = messagebox.askyesno(
            title="Unsaved Changes",
            message="You have unsaved changes. Exit anyway?")
        if not answer:
            return
    parent.destroy()
