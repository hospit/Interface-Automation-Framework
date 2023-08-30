import requests
import os
from utils.logging_tool.logging_tool import ERROR
# 输入pip install requests_toolbelt 安装依赖库


def file_path(path):
    if os.path.exists(path):
        # with open(path, 'r', encoding='utf-8') as file:
        #     f = file.read()
        # return f
        return open(path, 'rb')
    else:
        ERROR.logg.error(f"{path}->文件不存在")


def uploadImage():
    url = "https://open.feishu.cn/open-apis/im/v1/images"

    data = {'image_type': 'message'
            }  # 需要替换具体的path

    flies = {'image': open('/Users/alvis/Pictures/My_photo/8k/2ccfd943f36b27bdaa6659cc3872b75a.jpg', 'rb')}
    headers = {
        'Authorization': 'Bearer t-g1046aeb3EZJYWFLPDHQZIJV2A6ASQ6GWJBKLEYT',  ## 获取tenant_access_token, 需要替换为实际的token
    }

    res = requests.request("POST", url, headers=headers, files=flies, data=data)
    print(res.text)
    print(res.headers['X-Tt-Logid'])  # for debug or oncall
    print(res.content)  # Print Response







if __name__ == '__main__':
    uploadImage()