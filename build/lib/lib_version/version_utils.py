from importlib import metadata

def get_version() -> str:
    return metadata.version(__package__ or "lib-version")
def print_version() -> str:
    print(get_version())
    return "done"