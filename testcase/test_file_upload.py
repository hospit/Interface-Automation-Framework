import pytest
from utils.cache_tool.cachetool import CacheHandler, GetTestCase
from utils.requeststool.requests_tool import RequestsContorl


case_id = ['fileupload01']
case_data = GetTestCase.case_data(case_id)

class TestFileUpload:

    @pytest.mark.parametrize("upload", case_data, ids=case_id)
    def test_fileupload(self, upload):
        print(upload)
        res = RequestsContorl(upload).http_requests()
        print(res.text)

# class Testdep2():
#     @pytest.mark.dependency()
#     def test_01(self):
#         print('class test_01')
#         assert 1 == 1
#
#     @pytest.mark.dependency()
#     def test_02(self):
#         print('class test_02')




if __name__ == '__main__':
     pytest.main(['-sv'])
