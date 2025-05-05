from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("lib_version")
except PackageNotFoundError:
    __version__ = "0.0.0"

from .version_utils import VersionUtil
