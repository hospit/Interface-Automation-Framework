import pytest
from utils.cache_tool.cachetool import CacheHandler, GetTestCase
from utils.requeststool.requests_tool import RequestsContorl
from utils.assert_tool.assert_control import AassertCode

case_id01 = ['DumpImage01']

case_data01 = GetTestCase.case_data(case_id01)

case_id02 = ['create01']

case_data02 = GetTestCase.case_data(case_id02)


class TestDump:

    @pytest.mark.parametrize("dump", case_data01, ids=case_id01)
    def test_fileupload(self, dump):
        res = RequestsContorl(dump).http_requests()
        AassertCode(res_data=res.json(), status_code=res.status_code, assert_data=dump.get('assert')).assert_type_handle()

    @pytest.mark.parametrize('create', case_data02, ids=case_id02)
    def test_create(self, create):
        response = RequestsContorl(create).http_requests()
        # assert response.status_code == 200, f"创建订阅号文章: {response.text}"
        # set_global_data("message_id", response.json()["data"]["message_id"])
        AassertCode(res_data=response.json(), status_code=response.status_code, assert_data=create.get('assert')).assert_type_handle()


if __name__ == "__main__":
    pytest.main(['-vs'])