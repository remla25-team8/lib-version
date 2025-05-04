from importlib.metadata import version

class VersionUtil:
    @staticmethod
    def print_version():
        print(version("lib_version"))

    @staticmethod
    def get_version():
        return version("lib_version")