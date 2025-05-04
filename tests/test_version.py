from lib_version import VersionUtil
import re

def test_version_semver():
    VersionUtil.print_version()
    assert re.match(r"^\d+\.\d+\.\d+(\.\w+)?$", VersionUtil.get_version())