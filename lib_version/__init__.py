from importlib.metadata import version, PackageNotFoundError

def get_version() -> str:
    """
    Return the installed package version, e.g. '0.1.0'.
    If the package is not installed (running from source), return '0.0.0-pre'.
    """
    try:
        return version(__name__.replace('_', '-'))  # package name = lib-version
    except PackageNotFoundError:
        return "0.0.0-pre"
