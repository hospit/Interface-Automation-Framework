import requests
import pytest
import re
import cicd_backup_test.Datas.Domain_path as Domain_path
import cicd_backup_test.Datas.headers_ids as headers_ids


def test_calendar_create(get_token, set_global_data):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["创建日历"]
    header = get_token("tenant_token_header")
    json = {
        "summary": "api日历",
        "description": "API日历描述",
        "permissions": "public",
        "color": -1,
        "summary_alias": "日历备注名"
    }
    response = requests.request("post", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"创建日历: {response.text}"
    set_global_data("calendar_id", response.json()["data"]["calendar"]["calendar_id"])


def test_get_owner_calendar(get_token):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["获取主日历"]
    header = get_token("tenant_token_header")
    response = requests.request("post", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取主日历: {response.text}"


def test_get_calendar(get_token, get_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id"), Domain_path.calendars_path["获取日历"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取日历: {response.text}"


def test_calendar_list(get_token):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["获取日历列表"]
    header = get_token("tenant_token_header")

    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"xxx: {response.text}"


def test_update_calendar_list(get_token, get_global_data, set_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id"), Domain_path.calendars_path.get("更新日历"))
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    json = {
        "summary": "API测试日历更新",
        "description": "API使用开放接口创建日历",
        "permissions": "public",
        "color": -1,
        "summary_alias": "日历备注名"
    }
    response = requests.request("patch", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"更新日历: {response.text}"
    set_global_data("calendar_id_update", response.json()["data"]["calendar"]["calendar_id"])


def test_search_calendar(get_token):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["搜索日历"]
    header = get_token("tenant_token_header")
    json = {
        "query": "测试日历"
    }
    response = requests.request("post", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"搜索日历: {response.text}"
    assert response.json()["data"] is not None


def test_subscribe_calendar(get_token, get_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id_update"), Domain_path.calendars_path["订阅日历"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    response = requests.request("post", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"订阅日历: {response.text}"


def test_cancel_subscribe_calendar(get_token, get_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id_update"), Domain_path.calendars_path["取消订阅日历"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")

    response = requests.request("post", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"取消订阅日历: {response.text}"


def test_subscribe_calendar_event(get_token):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["订阅日历变更事件"]
    header = get_token("user_token_header")

    response = requests.request("post", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"订阅日历变更事件: {response.text}"


def test_cancel_subscribe_calendar_event(get_token):
    url = Domain_path.cicd_domain + Domain_path.calendars_path["取消订阅日历变更事件"]
    header = get_token("user_token_header")

    response = requests.request("post", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"取消订阅日历变更事件: {response.text}"



if __name__ == "__main__":
    pytest.main()











