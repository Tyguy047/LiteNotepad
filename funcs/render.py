"""
Used to render Markdown and HTML in a new window.

It is important to note that this is a basic render.
If an HTML file is being rendered, it will not use any CSS outside the current HTML file.
Buttons will not open other HTML files in the preview, and JS will not work at all.

This feature is intended for previewing Markdown but will also work for a basic preview of HTML.
"""

import tkinter as tk
from tkinterweb import HtmlFrame
import markdown

def render(workspace, parent):
    content = workspace.get("1.0", tk.END)
    html = markdown.markdown(content, extensions=["tables", "fenced_code"])

    popup = tk.Toplevel(workspace)
    popup.title("Preview")
    popup.transient(parent)

    scale = workspace.winfo_fpixels('1i') / 96
    popup.geometry(f"{int(600 * scale)}x{int(500 * scale)}")

    preview = HtmlFrame(popup, messages_enabled=False)
    preview.load_html(html)
    preview.pack(fill="both", expand=True)