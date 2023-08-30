import pytest
import os

if __name__ == "__main__":
    # pytest.main(['-vs','./testcase/test_token.py'])
    # pytest.main(['-vs','./testcase/test_file_upload.py'])
    pytest.main(['-vs', './testcase/test_dump_image.py'])
    # pytest.main(['-vs'])

    os.system("allure generate ./temp/logjson -o ./report --clean")

