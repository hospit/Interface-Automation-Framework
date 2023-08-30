import pytest
from utils.requeststool.requests_tool import RequestsContorl
from utils.yaml_read_tools.yamlfileread import YamlRead
from utils.yaml_read_tools.yamldatacontrol import YamlControl
data_login = YamlRead("\\datas").run()
# print(YamlControl(data_login).case_process())
case = YamlControl(data_login).run()


class TestToken():
    case_id = ['token01']
    case_data = []
    for i in case_id:
        case_data.append(case.get(i))

    # @pytest.mark.parametrize('token', case_data, ids=case_id)
    @pytest.mark.dependency(name="token")
    def test_01(self):
        print('function test_01')
        assert 1 == 1
    # @pytest.mark.dependency()
    # def test_token(self, token):
    #     print(token)
    #     assert 1 == 1

if __name__ == '__main__':
     pytest.main(['-sv'])
