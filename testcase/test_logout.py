import pytest
import requests

from utils.requeststool.requests_tool import RequestsContorl
from utils.yaml_read_tools.yamlfileread import YamlRead
from utils.yaml_read_tools.yamldatacontrol import YamlControl
data_logout = YamlRead("\\datas").run()
# print(YamlControl(data_login).case_process())
case = YamlControl(data_logout).run()
case_id = ['logout01']
case_data = []
for i in case_id:
    case_data.append(case.get(i))


class TestLogin:

    @pytest.mark.parametrize("logout", case_data, ids=case_id)
    def test_login(self, logout):
        # url = login.get("path")
        # method = login.get('method')
        # params = login.get('params')
        print(logout)
        #
        # res = RequestsContorl.requests(url=url, method=method, params=params)
        # print(res.json())
        # req = logout
        # res = RequestsContorl.requests(**req)
        # print(res.text)

if __name__ == "__main__":
    pytest.main("-vs")

if __name__ == "__main__":
    pytest.main("-vs")

