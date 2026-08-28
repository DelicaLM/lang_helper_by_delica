from .Word import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("lang_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["Word.py"]
