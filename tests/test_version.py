from lib_version import get_version
import re

def test_version_semver():
    semver_regex = r"^\d+\.\d+\.\d+$"
    assert re.match(semver_regex, get_version())
