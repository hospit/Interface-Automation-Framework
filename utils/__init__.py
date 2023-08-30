from utils.yaml_read_tools.yamlfileread import YamlRead
from utils.yaml_read_tools.yamldatacontrol import YamlControl
from common.setting import ensure_path_sep
from utils.cache_tool.cachetool import CacheHandler


# 每次执行先 把缓存的依赖文件 删除，防止又重复数据
# 开始时删除，会导致依赖数据 找不到该文件，读取，会报错，删除后应加上创建一个空文件，或者把删除文件该为清空文件数据
# YamlControl.delete_yaml(ensure_path_sep('/temp/temp_cache.yaml'))
YamlRead.delete_data(ensure_path_sep('/temp/temp_cache.yaml'))
# 调用 yamlread 工具 获取 用例数据
data_yaml = YamlRead("\\datas").run()
data = YamlControl(data_yaml).run()

for i in data:
    # print(data)
    CacheHandler.update_cache(i)
# CacheHandler.showcache()