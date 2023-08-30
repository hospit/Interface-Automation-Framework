# import pytest
# from utils.requeststool.requests_tool import RequestsContorl
# from utils.yaml_read_tools.yamlfileread import YamlRead
# from utils.yaml_read_tools.yamldatacontrol import YamlControl
# data_login = YamlRead("\\datas").run()
# # print(YamlControl(data_login).case_process())
# case = YamlControl(data_login).run()
# case_id = ["login01", "login02"]
# case_data = []
# for i in case_id:
#     case_data.append(case.get(i))
import pytest
from utils.cache_tool.cachetool import CacheHandler, GetTestCase
from utils.requeststool.requests_tool import RequestsContorl


case_id = ['fileupload01']
case_data = GetTestCase.case_data(case_id)


class TestLogin:

    @pytest.mark.parametrize("login", case_data, ids=case_id)
    def test_login(self, login):
        # url = login.get("path")
        # method = login.get('method')
        # params = login.get('params')
        print(login)
        #
        # res = RequestsContorl.requests(url=url, method=method, params=params)
        # print(res.json())
        # req = login
        # res = RequestsContorl.requests(**req)
        # print(res.text)


if __name__ == "__main__":
    pytest.main(["-vs"])

