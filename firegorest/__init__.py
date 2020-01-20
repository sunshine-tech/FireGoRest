import re
import sys
from pathlib import Path

from .doctools import tidy_doc    # NOQA


pyver = (sys.version_info.major, sys.version_info.minor)
if pyver <= (3, 7):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


def get_version():
    try:
        return importlib_metadata.version('firegorest')
    except importlib_metadata.PackageNotFoundError:
        pass
    # Run from development working folder
    filepath = Path(__file__).parent.parent / 'pyproject.toml'   # type: Path
    match = re.search('version = "([.0-9]+)"', filepath.read_text())
    return match.group(1)


__version__ = get_version()
