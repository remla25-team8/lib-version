from lib_version import print_version, get_version
import re

def test_version_semver():
    print_version()
    assert re.match(r"^\d+\.\d+\.\d+(\.\w+)?$", get_version())
