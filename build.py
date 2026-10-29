import os
import PyInstaller.__main__

icon = "assets/images/icon.ico"

PyInstaller.__main__.run([
    "main.py",
    "--onefile",
    "--windowed",
    "--name", "LiteNotepad",
    "--icon", icon,
    "--add-data", f"{icon}{os.pathsep}assets/images",
    "--collect-all", "binaryornot",
    "--clean",
])