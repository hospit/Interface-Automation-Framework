import pytest
import os

if __name__ == "__main__":
    # pytest.main(["-vs", "--alluredir", "./logs", "--reruns=1"])
    pytest.main(["-vs", "./testcase/test_subscriptions/test_subscriptions.py::test_create"])
    os.system("allure generate ./logs -o ./logs/html --clean")
