from .save import save
from .close import close
from .load import load
from .undo import undo
from .redo import redo
from .fonts import font_face, font_size, change_font_face, change_font_size

__all__ = [
    "save",
    "close",
    "load",
    "undo",
    "redo",
    "font_face",
    "font_size",
    "change_font_face",
    "change_font_size"
]