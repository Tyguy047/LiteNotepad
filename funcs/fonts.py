import json
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import simpledialog, font

def font_face(config_file):
    with open(config_file, "r") as f:
        return json.load(f)["font_face"]

def font_size(config_file):
    with open(config_file, "r") as f:
        return json.load(f)["font_size"]

def change_font_face(config_file, workspace, parent):
    fonts = sorted(set(font.families()))
    fonts = [f for f in fonts if not f.startswith("@")]

    popup = tk.Toplevel(workspace)
    popup.title("Choose Font")
    popup.transient(parent)

    scale = workspace.winfo_fpixels('1i') / 96
    popup.geometry(f"{int(300 * scale)}x{int(400 * scale)}")

    font_list = ScrolledText(popup, cursor="hand2")
    font_list.pack(fill="both", expand=True)

    def pick(name):
        with open(config_file, "r") as f:
            settings = json.load(f)

        settings["font_face"] = name

        with open(config_file, "w") as f:
            json.dump(settings, f)

        workspace.configure(font=(name, settings["font_size"]))
        popup.destroy()

    for i, name in enumerate(fonts):
        tag = f"font_{i}"
        font_list.insert("end", name + "\n", tag)
        font_list.tag_bind(tag, "<Button-1>", lambda e, n=name: pick(n))
        font_list.tag_configure(tag, font=(name, 12))

    font_list.configure(state="disabled")

def change_font_size(config_file, workspace, parent):
    size = simpledialog.askinteger("Font Size", "Enter size:", parent=parent, minvalue=7, maxvalue=72)

    if size is None:
        return

    with open(config_file, "r") as f:
        settings = json.load(f)

    settings["font_size"] = size

    with open(config_file, "w") as f:
        json.dump(settings, f)

    workspace.configure(font=(settings["font_face"], size))