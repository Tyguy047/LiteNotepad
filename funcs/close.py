def close(workspace):
    workspace.delete("1.0", "end")
    workspace.file_path = None