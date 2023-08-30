import re
from utils.yaml_read_tools.yamlfileread import YamlRead
from common.setting import ensure_path_sep
import ast




def cache_regular(case_data: str):
    """
    通过正则的方式，替换case_data中依赖数据标识 例：$cache{login_init} 为 依赖数据
    :param case_data: 用例数据
    :param _cache_data: 从依赖文件中读取的依赖数据
    :return:
    """

    # 正则获取 $cache{login_init}中的值 --> login_init
    regular_dates = re.findall(r"\$cache\{(.*?)\}", case_data)

    # 拿到的是一个list，循环数据
    for regular_data in regular_dates:
        pattern = re.compile(
                r'\$cache\{' + regular_data.replace('$', "\$").replace('[', '\[') + r'\}'
            )
        try:
            # cache_data = Cache(regular_data).get_cache()
            _cache_data = YamlRead.read_yaml_data(ensure_path_sep('/temp/temp_cache.yaml'))
            cache_data = _cache_data.get(regular_data)
            # 使用sub方法，替换已经拿到的内容
            case_data = re.sub(pattern, str(cache_data), case_data)
        except Exception:
            print(" exception -------------------")
            pass
    return case_data



if __name__ == "__main__":
    """
    from common.setting import ensure_path_sep
    from utils.yaml_read_tools.yamlfileread import YamlRead
    from utils.yaml_read_tools.yamldatacontrol import YamlControl
    data_logout = YamlRead("\\datas").run()
    case = YamlControl(data_logout).run()

    data = YamlRead.read_yaml_data(ensure_path_sep('/temp/temp_cache.yaml'))

    aa = cache_regular(case_data=str(case), _cache_data=data)
    print(aa)
    """
