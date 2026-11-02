from tkinter import messagebox

def close(workspace):
    if not workspace.saved:
        answer = messagebox.askyesno(
            title="Unsaved Changes",
            message="You have unsaved changes. Close the file anyway?")
        if not answer:
            return

    workspace.delete("1.0", "end")
    workspace.file_path = None
    workspace.saved = True
    workspace.edit_reset()
    workspace.edit_modified(False)