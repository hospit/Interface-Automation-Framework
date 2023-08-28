import pytest
import requests
import cicd_backup_test.Datas.Domain_path as Domain_path
import cicd_backup_test.Datas.headers_ids as headers_ids
import os

token_datas = {}

@pytest.fixture(scope="session", autouse=True)
def set_token():
    def tenant_access_token():
        # 获取tenand_token
        tenand_url = f"{Domain_path.cicd_domain}/open-apis/auth/v3/tenant_access_token/internal"

        tenand_response = requests.post(url=tenand_url, headers=headers_ids.appid_headers["code_tenant_header"], json=headers_ids.appid_datas["appid_appsecret_data"])
        assert tenand_response.status_code == 200, f"tenant_access_token报错: {tenand_response.text}"
        print("\n前置操作tokem-----")
        return tenand_response.json()["tenant_access_token"]
        # print(tenand_response.text)

    def codes():
        # 获取code
        code_url = f"{Domain_path.cicd_domain}/open-apis/mina/v2/login"
        header = {
            "Authorization": "Bearer " + tenant_access_token(),
            "Content-Type": "application/json;charset=utf-8"
        }
        data = headers_ids.appid_datas["code_data"]
        code_response = requests.post(url=code_url, headers=header, json=data)
        try:
            assert code_response.json()["data"]["code"] is not None
            # print("获取code", code_response.text)]
            print("\n前置操作code-----")
            return code_response.json()["data"]["code"]
        except:
            print(code_response.json())
            print("sessionid过期；请更改 headers_ids 文件里的，sessionid 值")
            os._exit(0)

    def user_access_token():
        # 获取user_token
        url = f"{Domain_path.cicd_domain}/open-apis/mina/loginValidate"
        data = headers_ids.appid_datas["appid_secret_data"]
        data.update({"code": str(codes())})
        user_response = requests.post(url=url, headers=headers_ids.appid_headers["code_tenant_header"], json=data)
        # print("user_token", user_response.content)
        assert user_response.json()["access_token"] is not None, f"tenant_access_token报错: {user_response.content}"
        print("\n前置操作user-----")
        return user_response.json()["access_token"]

    def app_access_token():
        url = f"{Domain_path.cicd_domain}/open-apis/auth/v3/app_access_token/internal"
        app_data = {
            "app_id": "",
            "app_secret": ""
        }
        app_response = requests.post(url=url, headers=headers_ids.appid_headers["code_tenant_header"], json=app_data)
        assert app_response.json()["code"] == 0
        # print("user_token", app_response.content)
        return app_response.json()["app_access_token"]

    def token_data(key):
        datas = {
                "tenant_token_header": {
                    "Authorization": "Bearer " + str(tenant_access_token()),
                    "Content-Type": "application/json;charset=utf-8"
                },
                "user_token_header": {
                    "Authorization": "Bearer " + str(user_access_token()),
                    "Content-Type": "application/json;charset=utf-8"
                },
                "app_token_header": {
                    "Authorization": "Bearer " + str(app_access_token()),
                    "Content-Type": "application/json;charset=utf-8"
                }
        }
        token_datas.update(datas)
        print("\n前置操作-----")
    return token_data


@pytest.fixture()
def get_token():
    def _get_token(key):
        return token_datas.get(key)
    return _get_token


global_data = {}


@pytest.fixture
def set_global_data():
    def _set_global_data(key, value):
        global_data[key] = value
    return _set_global_data


@pytest.fixture
def get_global_data():
    def _get_global_data(key):
        return global_data.get(key)
    return _get_global_data