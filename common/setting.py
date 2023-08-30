import os
from typing import Text


def root_path():
    """ 获取项目根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    """
    os.path.abspath: 返回绝对路径
    __file__: 表示当前文件
    os.path.dirname：返回上一层文件夹绝对路径
    """
    return path


def ensure_path_sep(path) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))
    if "\\" in path:
        path = os.sep.join(path.split("\\"))
    """
    os.sep.join(): 函数传入的参数是一个列表，输出的结果是将列表中的元素用相应平台对应的路径分隔符链接起来的整体
    """
    return root_path() + path


if __name__ == "__main__":
    print(ensure_path_sep("\\logs\\"))
