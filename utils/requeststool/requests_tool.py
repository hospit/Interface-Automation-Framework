import requests
from utils.logging_tool.logging_tool import ERROR, DEBUG
# from utils.requeststool.file_upload import file_path
from utils.api_dependent.dependent_cache import cache_regular
import ast



class RequestsContorl:
    """
    封装请求
    """
    def __init__(self, case_data):
        self._case_data = case_data
        # self._case_data = cache_regular(str(case_data))


    def http_requests(self):
        # from 导入写在 函数里，而不是，文件头
        # 因为 dependent_tool 文件中有导入，此文件，写在开头，会陷入导入死循环，进而报错
        from utils.api_dependent.dependent_tool import DependentControl
        # 依赖数据获取 要写在 if——requestType() 前面。
        # 因为，获取依赖数据后，要把 case_data 依赖标识替换成依赖数据
        # 且因为 DependentControl 和 RequestsContorl 循环无法 替换 起始的case_data
        # 及把 替换起始case_data 数据 写在 self.if_requestType()中，所以获取依赖数据要在self.if_requestType()前
        DependentControl(self._case_data).run()
        # 判断类型，发送请求
        _res = self.if_requestType()
        return _res

    def if_requestType(self):
        if self._case_data.get('requestType') == 'file':
            for key, values in self._case_data['data']['file'].items():
                if values is not None:
                    file = {key: open(values, 'rb')}
                    data = self._case_data.get('data')['data']
                    res = self.requests(
                                        #写在here，解决连续 依赖case情况
                                        # 例 case1 依赖 case2 ，case2 依赖 case3
                                        url=cache_regular(self._case_data.get('url')),
                                        method=self._case_data.get('method'),
                                        headers=ast.literal_eval(cache_regular(str(self._case_data.get('headers')))),
                                        files=file,
                                        params=self._case_data.get('params'),
                                        data=data
                                        )
                    return res
                else:
                    ERROR.logg.error("yaml 数据 file为空")
        elif self._case_data.get('requestType') == 'json':
            res = self.requests(
                        url=cache_regular(self._case_data.get('url')),
                        method=self._case_data.get('method'),
                        headers=ast.literal_eval(cache_regular(str(self._case_data.get('headers')))),
                        params=self._case_data.get('params'),
                        json=self._case_data.get('json')
            )
            return res
        elif self._case_data.get('requestType') == 'data':
            res = self.requests(
                        method=self._case_data.get('method'),
                        url=cache_regular(self._case_data.get('url')),
                        data=self._case_data.get('data'),
                        headers=ast.literal_eval(cache_regular(str(self._case_data.get('headers'))))
            )


    @classmethod
    def requests(cls, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        try:
            """
            封装request请求，将请求方法、请求地址，请求参数、请求头等信息入参。
            注 ：verify: True/False，默认为True，认证SSL证书开关；cert: 本地SSL证书。如果不需要ssl认证，可将这两个入参去掉
            """
            res = requests.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)
            DEBUG.logg.info(
                f"\n请求状态：{res.status_code} \n请求地址：{url} \n请求方法：{method} \n 请求头{res.request.headers}, \n 请求body{data}"
                f"\n请求参数：{data,json} "
                # f"\n响应头：{res.headers} "
                f"\n响应结果：{res.text}"
            )
            # 返回响应结果
            return res
        # 异常处理 报错显示具体信息
        except Exception:
            # 打印异常
            ERROR.logg.exception(f"requests Exception", exc_info=True)




# if __name__ == "__main__":
    # # print(RequestsContorl.requests(method='get', url='/user/login'))
    # from utils.yaml_read_tools.yamlfileread import YamlRead
    # from utils.yaml_read_tools.yamldatacontrol import YamlControl
    # data_login = YamlRead("\\datas").run()
    # case = YamlControl(data_login).run()
    # case_id = ['fileupload01']
    # case_data = []
    # for i in case_id:
    #     case_data.append(case.get(i))
    #
    # # print(case_data)
    # aa = case_data[0]
    # # print(aa)
    # print(RequestsContorl().if_requestType(aa))
