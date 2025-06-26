from . import __version__

class VersionUtil:
    @staticmethod
    def print_version():
        print(__version__)

    @staticmethod
    def get_version():
        return __version__