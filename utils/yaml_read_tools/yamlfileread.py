import os
# from typing import Text
import yaml
from common.setting import ensure_path_sep


class YamlRead:
    def __init__(self, path):
        self.path = path

    def get_yaml_path(self, file_path) -> list:
        """
        用于获取所有yaml文件的绝对路径
        :param file_path:
        :return: 以list类型 all yaml文件绝对路径
        """
        filename = []
        # 获取所有文件下的子文件名称
        for root, dirs, files in os.walk(file_path):
            for _file_path in files:
                if 'yaml' in _file_path or '.yaml' in _file_path:
                    path = os.path.join(root, _file_path)
                    filename.append(path)
        return filename

    @classmethod
    def read_yaml_data(cls, file_dir) -> dict:
        """
        获取 yaml 中的数据
        :param: fileDir: 文件路径
        :return:
        """
        # 判断文件是否存在
        if os.path.exists(file_dir):
            with open(file_dir, 'r', encoding='utf-8') as f:
                res = yaml.load(f, Loader=yaml.FullLoader)
                if res is None:
                    res = {}
        else:
            raise FileNotFoundError("文件路径不存在")
        return res

    @classmethod
    def delete_data(cls, _path):
        with open(_path, 'w') as f:
            f.truncate()

    def run(self):
        data_list = []
        for i in self.get_yaml_path(ensure_path_sep(self.path)):
            data_list.append(self.read_yaml_data(i))
            # print(self.read_yaml_data(i),"22")
        return data_list


if __name__ == "__main__":
    # print(YamlRead("\\datas").run())
    # YamlRead.run_yaml_data(
    # print(YamlRead("\\datas\\login.yaml").ensure_path_sep())
    YamlRead.delete_data(ensure_path_sep('//temp/temp_cache.yaml'))
