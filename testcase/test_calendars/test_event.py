import requests
# import pytest
import re
import cicd_backup_test.Datas.Domain_path as Domain_path
import time


def test_event_create(get_token, get_global_data, set_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id"), Domain_path.events_path["创建日程"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    json = {
        "summary": "API日程",
        "description": "日程API描述",
        "need_notification": False,
        "start_time": {
            "date": str(time.strftime("%Y-%m-%d", time.localtime())),
            "timestamp": str(int(time.time())),
            "timezone": "Asia/Shanghai"
        },
        "end_time": {
            "date": str(time.strftime("%Y-%m-%d", time.localtime())),
            "timestamp": str(int(time.time()+3600)),
            "timezone": "Asia/Shanghai"
        },
        "visibility": "default",
        "attendee_ability": "can_see_others",
        "free_busy_status": "busy",
        "color": -1
    }
    response = requests.request("post", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"创建日程: {response.text}"
    set_global_data("event_id", response.json()["data"]["event"]["event_id"])


def test_get_event(get_token, get_global_data):
    path = re.sub(":event_id", get_global_data("event_id"), Domain_path.events_path["获取日程"])
    path = re.sub(":calendar_id", get_global_data("calendar_id_update"), path)
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")

    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取日程: {response.text}"


def test_event_update(get_token, get_global_data, set_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id_update"), Domain_path.events_path["更新日程"])
    path = re.sub(":event_id", get_global_data("event_id"), path)
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    json = {
        "summary": "title_of_test",
        "description": "this_a_test",
        "start_time": {
            "timestamp": str(int(time.time()+3600)),
            "timezone": "Asia/Shanghai"
        },
        "end_time": {
            "timestamp": str(int(time.time()+3600*2)),
            "timezone": "Asia/Shanghai"
        },
        "vchat": {
            "meeting_url": "https://vc.feishu.cn/j/769261640"
        },
        "visibility": "default",
        "attendee_ability": "can_see_others",
        "free_busy_status": "busy",
        "location": {
            "name": "test_pleace",
            "address": "地点地址",
            "latitude": 116.43789924628962,
            "longitude": 39.87853566148457
        },
        "color": -1,
        "reminders": [
            {
                "minutes": 60
            }
        ]
    }
    response = requests.request("patch", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"更新日程: {response.text}"
    set_global_data("event_id_update", response.json()["data"]["event"]["event_id"])


def test_get_event_list(get_token, get_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id_update"), Domain_path.events_path["获取日程列表"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取日程列表: {response.text}"


def test_event_delete(get_token, get_global_data):
    path = re.sub(":calendar_id", get_global_data("calendar_id"), Domain_path.events_path["删除日程"])
    path = re.sub(":event_id", get_global_data("event_id_update"), path)
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")

    response = requests.request("delete", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"删除日程: {response.text}"










