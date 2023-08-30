from utils.requeststool.requests_tool import RequestsContorl
from utils.cache_tool.cachetool import CacheHandler
from common.setting import ensure_path_sep
from jsonpath import jsonpath
import yaml
import ast
from utils.api_dependent.dependent_cache import cache_regular
# 2023-08-27 追加： 未解决重复请求问题
from utils.yaml_read_tools.yamlfileread import YamlRead



class DependentControl:
    """

    """
    def __init__(self, case_data):
        """
        :param case_data: 用例数据 以列表形式传入 例：
        {'testcase01':{'host': 'https://...', 'path': '/ope..', 'method': 'POST'}}
        """
        self._case_data = case_data
        self._temp_path = ensure_path_sep('/temp/temp_cache.yaml')
    @classmethod
    def get_cache(cls, case_id) :
        """
        获取缓存用例池中的数据，通过 case_id 提取
        :param case_id:
        :return: case_id_01
        """
        _case_data = CacheHandler.get_cache(case_id)
        return _case_data

    def analyze(self):
        """
        提取 case_data里 dependence_case 和 dependence_case_data，进行是否有依赖数据判断
        有依赖数据 者进行下步操作
        :return:
        """
        _dep_data = self._case_data.get('dependence_case')
        _req_data = self._case_data.get('dependence_case_data')
        if _dep_data is True:
            if _req_data is not None:
                # 加for 是因为 yaml dependence_case_data 的value 是列表格式，
                # 设置成列表格式 是处理 多个依赖数据情况，所以这里要for 确保每个依赖都获取
                for i in _req_data:
                    # 从 缓存 池 中 获取，依赖case数据
                    _new_data = self.get_cache(i.get('case_id'))
                    # 替换 case中的依赖数据，可以 防止其它 case 获取到依赖数据后，重复请求
                    # 2023-08-27 追加： 这里 替换依赖数据并没有 实现防止重复请求
                    _new_case_data = ast.literal_eval(cache_regular(str(_new_data)))
                    # 2023-08-27 变动：将依赖请求移动至 下方，but 当一个依赖结果有多个依赖数据 ，会重复请求
                    # _res = RequestsContorl(_new_case_data).http_requests()
                    # dependent_data的value 为列表，是用例处理 一个依赖接口中有多个依赖 数据
                    for _dep_data in i.get('dependent_data'):
                        # 2023-08-27 追加： 由于上方并 为解决重复请求问题，下方加个依赖数据是否存在判断 来防止，依赖数据重复写入
                        # 2023-08-27 追加：在YamlRead.read_yaml_data 函数中 加来，读取为None，者返回{}
                        _cache_data = YamlRead.read_yaml_data(ensure_path_sep('/temp/temp_cache.yaml'))
                        # 2023-08-27 追加：当get dict没有时返回None，不能 直接 None is False 判断，该判断 为False
                        if not _cache_data.get(_dep_data.get('set_cache')):
                            # 请求 case获取依赖数据，并且请求模块中有 调用dependent_tool模块 解决连续依赖问题
                            _res = RequestsContorl(_new_case_data).http_requests()

                            _cache = self.dependent_jsonpath(_dep_type=_dep_data.get('dependent_type'),
                                                                 _res=_res,
                                                                 _dep_jsonpath=_dep_data.get('jsonpath'),
                                                                 _dep_set_cache=_dep_data.get('set_cache')
                                                                 )
                            self.dep_write_temporary(_cache_data=_cache)
                # 加返回 为了 下方 def run 中，判断 case是否有依赖，有则替换依赖
                return True
        else:
            return False


    def dependent_jsonpath(self, _dep_type, _res, _dep_jsonpath, _dep_set_cache):
        """
        :param _dep_type: dependent_type 用来判断 依赖数据是否 响应response中
        :param _res: 请求返回的数据，及dependent_requests 函数的返回
        :param _dep_jsonpath: jsonpath 语法，用来提取 返回数据中的依赖数据
        :param _dep_set_cache: 自定义依赖数据名称，用来绑定依赖数据
        :return: 依赖数据字典格式
        """
        if _dep_type == 'response':
            _dep_data = jsonpath(_res.json(), _dep_jsonpath)[0]
            # self._cache_dict = {_dep_set_cache: _dep_data}
            return {_dep_set_cache: _dep_data}
        else:
            print("dependent_type is None or response填写错误,请检查 case yaml data")

    def dep_write_temporary(self, _cache_data):
        """
        将获取的依赖数据 写入到yaml文件中
        :param _cache_data: 字典格式的依赖数据
        :param self._temp_path: 临时数据路径，先判断 该路径文件是否存在，不存在则 创建
        :return:
        """
        with open(self._temp_path, 'a', encoding="utf-8") as file:
            yaml.dump(data=_cache_data, stream=file, allow_unicode=True)

    def run(self):
        self.analyze()
        # if self.analyze() is True:
            # self._case_data = cache_regular(case_data=str(self._case_data))
            # pass



if __name__ == "__main__":
    from utils.yaml_read_tools.yamlfileread import YamlRead
    from utils.yaml_read_tools.yamldatacontrol import YamlControl
    data_logout = YamlRead("\\datas").run()
    data = YamlControl(data_logout).run()
    DependentControl(data).run()
    # YamlControl.delete_yaml(ensure_path_sep('/temp/temp_cache.yaml'))
    # DependentControl(data_logout).run()
    # for i in data_logout:
        # for key, value in i.items():
        #     DependentControl(value).run()
    # case = YamlControl(data_logout).run()
    # case_id = 'fileupload01'
    # case_datas = case.get(case_id)
    '''
    res, dep_type, dep_jsonpath, dep_set = dependentreq(case_data)

    dep = depif(res, dep_type, dep_jsonpath, dep_set)
    

    dep_write_temporary(dep, path)
    '''
    # DependentControl(case_datas).run()

    path = '/Users/alvis/Code_Library/pythonProject/temp/temp_cache.yaml'
    # def readyam(_path):
    #     with open(_path, 'r', encoding='utf-8') as f:
    #         _res = yaml.load(f, Loader=yaml.FullLoader)
    #     return _res
    #
    # print(readyam(path))