from importlib.metadata import version, PackageNotFoundError

# Version will be injected by CI/CD workflow
__version__ = "0.0.0"

# Try to get version from metadata if available, otherwise use hardcoded version
try:
    __version__ = version("lib_version")
except PackageNotFoundError:
    # Keep the hardcoded version if metadata is not available
    pass

from .version_utils import VersionUtil
