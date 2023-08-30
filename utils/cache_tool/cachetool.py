
_cache_config = {}


class CacheHandler:
    @staticmethod
    def get_cache(cache_data):
        try:
            return _cache_config[cache_data]
        except KeyError:
            # raise ValueNotFoundError(f"{cache_data}的缓存数据未找到，请检查是否将该数据存入缓存中")
            print(f"{cache_data}的缓存数据未找到，请检查是否将该数据存入缓存中")

    @staticmethod
    # def update_cache(*, cache_name, value):
    #     _cache_config[cache_name] = value
    def update_cache(value):
        _cache_config.update(value)

    @classmethod
    def showcache(cls):
        print(_cache_config)


class GetTestCase:

    @staticmethod
    def case_data(case_id_lists: list):
        case_lists = []
        for i in case_id_lists:
            _data = CacheHandler.get_cache(i)
            case_lists.append(_data)

        return case_lists