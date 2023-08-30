from common.setting import ensure_path_sep
import yaml
import re
import os


class YamlFunctions:

    @classmethod
    def host(cls):
        path = ensure_path_sep("\\common\\common.yaml")
        with open(path, 'r', encoding='utf-8') as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        return res.get('host')

    @classmethod
    def feishu(cls):
        path = ensure_path_sep("\\common\\common.yaml")
        with open(path, 'r', encoding='utf-8') as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        return res.get('feishu')

    @classmethod
    def account_id(cls):
        path = ensure_path_sep("\\common\\common.yaml")
        with open(path, 'r', encoding='utf-8') as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        return res.get('account_id')



class YamlControl:

    def __init__(self, data):
        self.data = data

    def case_process(self, data) -> dict:
        """
        获取字典数据，yaml文件的 例：{'logout01': {'host': 'https://www.wanandroid.com', 'path': '/user/logout/json', 'method': 'get', 'headers': None, 'params': None}}
        将 host 和 path 合并，成url
        data = GetYamlData(self.file_path).get_yaml_data()
        """
        _case_dict = []
        for i in data:
            for key, values in i.items():

                # 公共配置中的数据，与用例数据不同，需要单独处理
                case_date = {
                    "url": values.get("host") + values.get("path"),
                    'method': values.get('method'),
                    'headers': values.get('headers'),
                    'params': values.get('params'),
                    'requestType': values.get('requestType'),
                    'json': values.get('json'),
                    'data': values.get('data'),
                    'dependence_case': values.get('dependence_case'),
                    'dependence_case_data': values.get('dependence_case_data'),
                    'assert': values.get('assert')
                }
                _case_dict.append({key: case_date})

        return _case_dict

    def regular(self) -> list:
        """
        新版本
        使用正则替换请求数据
        :return:
        """
        try:
            # 先将list数据转换成字符串
            target = str(self.data)
            # 正则表达式
            regular_pattern = r'\${{(.*?)}}'
            # 用正则 findall 方法 判断字符串中是否 用符合表达式的内容
            while re.findall(regular_pattern, target):
                # search 方法 匹配整个字符串，并返回第一个成功的匹配 的范围 类似迭代器， group 取匹配的第几个范围
                key = re.search(regular_pattern, target).group(1)
                value_types = ['int:', 'bool:', 'list:', 'dict:', 'tuple:', 'float:']
                # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
                # 为什么要加 这个判断 暂不清楚
                if any(i in key for i in value_types) is True:
                    func_name = key.split(":")[1].split("(")[0]
                    value_name = key.split(":")[1].split("(")[1][:-1]
                    if value_name == "":
                        value_data = getattr(YamlFunctions(), func_name)()
                    else:
                        value_data = getattr(YamlFunctions(), func_name)(*value_name.split(","))
                    regular_int_pattern = r'\'\${{(.*?)}}\''
                    target = re.sub(regular_int_pattern, str(value_data), target, 1)
                else:
                    # 以( 分割 匹配的字符串，以list返回，并取 第一位
                    func_name = key.split("(")[0]
                    # 以( 分割 匹配的字符串，以list返回，并取 第二位，then取字符串 0到倒数第二位
                    value_name = key.split("(")[1][:-1]
                    # 判断yaml 数据中的函数 是否带有参数
                    if value_name == "":
                        # getattr() 函数,结合re 实现字符串 函数调用
                        value_data = getattr(YamlFunctions, func_name)()
                    else:
                        value_data = getattr(YamlFunctions, func_name)(*value_name.split(","))
                    # 将字符串中的函数替换成调用函数返回的值
                    target = re.sub(regular_pattern, str(value_data), target, 1)
            return eval(target)

        except AttributeError:
            # ERROR.logger.error("未找到对应的替换的数据, 请检查数据是否正确 %s", target)
            raise
        except IndexError:
            # ERROR.logger.error("yaml中的 ${{}} 函数方法不正确，正确语法实例：${{get_time()}}")
            raise

    def run(self):
        return self.case_process(self.regular())

    @classmethod
    def delete_yaml(cls, path):
        """删除所有临时或缓存文件"""
        if not os.path.exists(path):
            # raise FileNotFoundError(f"您要删除的缓存文件不存在 {path}")
            print(f"您要删除的缓存文件不存在 {path}")
        else:
            os.remove(path)





if __name__ == "__main__":
    from utils.yaml_read_tools.yamlfileread import YamlRead
    aa = YamlRead("\\datas").run()
    # print(YamlControl(aa).case_process())
    # print(YamlControl.host())
    # bb = YamlControl(aa).regular()
    cc = YamlControl(aa).run()
    # print(type(bb))
    print(cc)
