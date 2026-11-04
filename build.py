import os
import sys
import PyInstaller.__main__

if sys.platform == "win32":
    icon = "assets/images/icon.ico"

else:
    icon = "assets/images/icon.png"

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