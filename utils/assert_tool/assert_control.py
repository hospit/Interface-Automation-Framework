import ast
import json
import types
from typing import Text, Dict, Any, Union
from jsonpath import jsonpath
from utils.assert_tool import assert_content

class AssertDataProcessing:
    def __init__(self, res_data, status_code, assert_data=""):
        self.assert_data = assert_data
        self.res_data = res_data
        self.status_code = status_code

    def get_assert_data(self):
        """"判断 assert data不为空，返回 errorcode data """
        assert self.assert_data, (
            "assert_data数据为空，请检查 yaml数据文件是否编写")
        return self.assert_data

    def assert_jsonpath(self):
        """ 获取jsonpath语法，用jsonpath方法 在响应数据中提取实际 数值，返回 """
        _reality = jsonpath(self.res_data, self.get_assert_data().get('jsonpath'))
        assert _reality, ('jsonpath 获取 实际值为空，请检查jsonpath语法')
        return _reality[0]

    def assert_type(self):
        """
        用vars() 函数 读取assert_content文件中属性和属性值的字典对象；
        用 isinstance() 函数 判断 and 提取字典对象中 为函数 的对象;
        """
        _asserttypedict = {}
        for key, value in vars(assert_content).items():
            if isinstance(value, types.FunctionType):
                # _asserttypedice.update({key, value})
                _asserttypedict[key] = value
        """create一个 function对应的 映射表"""
        _mapping_table = {
            'contains': 'in',
            'equal': '==',
            'greater': '>',
            'greater_equal': '>=',
            'inequality': '!=',
            'less': '<',
            'less_equal': '<='
        }
        """根据 value，check key"""
        _type = next(key for key, value in _mapping_table.items() if value == self.get_assert_data().get('type'))

        return _asserttypedict.get(_type)

    def assert_hanlder(self):

        self.assert_type()(self.assert_jsonpath(), self.get_assert_data().get('value'))


class AassertCode(AssertDataProcessing):

    def assert_type_handle(self):
        self.get_assert_data()   # 这里调用 是为了判断 是否有 yaml文件中是否编写了断言数据
        _assert_list = []
        for k, v in self.assert_data.items():
            if k == "status_code":
                assert v == self.status_code, "响应状态码断言失败"
            else:
                _assert_list.append(v)
        # _assert_list 不判断 是否有数据 是因为，有可能只需要状态码断言
        # 但 _assert_list 为空时，for 以下代码是不执行的
        for i in _assert_list:
            self.assert_data = i
            super().assert_hanlder()

    # def assert_data_list(self):
    #     assert_list = []
    #     for k, v in self.assert_data.items():
    #         if k == "status_code":
    #             assert self.status_code == v, "响应状态码断言失败"
    #         else:
    #             assert_list.append(v)
    #     return assert_list
    #
    # def assert_type_handle(self):
    #     self.get_assert_data()
    #     for i in self.assert_data_list():
    #         self.assert_data = i
    #         super().assert_hanlder()


if __name__ == "__main__":
    """
    需要传入data：
    yaml文件中 assert 数据
        {assert:{
              # 断言接口状态码
              errorCode:{
                        jsonpath: $.errorCode
                        type: ==
                        value: 0
                        AssertType:
                        }
              status_code: 200
              }
        }
    响应data
        res.data
    响应状态码
        res.status_code
        用来前置断言 响应状态是否 符合预期
    响应体
        request_data=res.body
        如何处理 res.body
        什么情况下 需要 body
    响应数据
        response_data=res.response_data
        如何处理 res.body
        什么情况下 需要 body

    """
    ass = {

        # # 断言接口状态码
        # 'errorCode': {
        #         'jsonpath': '$.errorCode',
        # 'type': '==',
        # 'value': 0,
        # 'AssertType':''
        # }
        # 'status_code': 200
        }
    res = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel1",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

    status_code = 200
    outcome = AassertCode(res_data=res, status_code=status_code, assert_data=ass).assert_type_handle()
    # outcome = AassertCode(res_data=res, status_code=status_code, assert_data=ass).get_assert_data()
    # print(outcome)






























