from lib_version import VersionUtil
import re

def test_version_server():
    VersionUtil.print_version()
    assert re.match(r"^\d+\.\d+\.\d+(\.\w+)?$", VersionUtil.get_version())
    
    
if __name__ == "__main__":
    test_version_server()
    print("All tests passed.")