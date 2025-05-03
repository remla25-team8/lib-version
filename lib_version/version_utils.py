from importlib.metadata import version

def print_version():
    print(version("lib_version"))

def get_version():
    return version("lib_version")