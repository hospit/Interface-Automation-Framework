import pytest
import requests
import re
# import pprint
import cicd_backup_test.Datas.Domain_path as Domain_path


def test_dump_image(get_token):
    url = Domain_path.cicd_domain + Domain_path.subscriptions_path["转存图片"]
    json = {
        "original_url": ""
    }
    header = get_token("tenant_token_header")
    response = requests.post(url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"转换图片：{response.text}"


def test_create(get_token, set_global_data):
    url = Domain_path.cicd_domain + Domain_path.subscriptions_path["创建订阅号文章"]
    header = get_token("tenant_token_header")
    json = {
        "articles": [
            {
                "title": "每日飞书小知识2345",
                "cover": {
                    "origin_cover": "",
                    "message_cover": "",
                    "article_cover": ""
                },
                "content": "<p>content here</p>",
                "external_link_url": "https://www.sample.cn",
                "article_type": 1,
                "content_source_url": "www.sample.com",
                "author": "飞书小助手",
                "i18n_title": {
                    "zh_cn": "API中文内容",
                    "en_us": "英文内容",
                    "ja_jp": "日本語の内容"
                },
                "i18n_content": {
                    "zh_cn": "123456中文内容",
                    "en_us": "英文内容",
                    "ja_jp": "日本語の内容"
                },
                "article_config": {
                    "allow_comment": True,
                    "allow_forward": True,
                    "share_type": 1,
                    "comment_display_type": 1
                },
                "digest": "这里是内容摘要"
            }
        ]
    }
    response = requests.post(url=url, headers=header, json=json)
    assert response.status_code == 200, f"创建订阅号文章: {response.text}"
    set_global_data("message_id", response.json()["data"]["message_id"])


def test_send(get_token, get_global_data):
    path = re.sub(":message_id", get_global_data("message_id"), Domain_path.subscriptions_path["发送订阅号文章"])
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    json = {
        "send_type": 1
    }
    response = requests.request("post", url=url, headers=header, json=json)
    assert response.status_code == 200, f"发送订阅号文章: {response.text}"
    assert response.json()["code"] == 0


def test_news_list(get_token):
    url = Domain_path.cicd_domain + Domain_path.subscriptions_path["获取订阅号消息（文章）列表"]
    header = get_token("tenant_token_header")
    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取订阅号消息（文章）列表: {response.text}"
    assert response.json()["data"] is not None


def test_news_content(get_token, get_global_data):
    path = re.sub(":message_id", get_global_data("message_id"), Domain_path.subscriptions_path.get("获取订阅号消息（文章）内容"))
    url = Domain_path.cicd_domain + path
    header = get_token("tenant_token_header")
    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取订阅号消息（文章）内容: {response.text}"


def test_accounts_list(get_token):
    url = Domain_path.cicd_domain + Domain_path.subscriptions_path["获取账号列表"]
    header = get_token("tenant_token_header")
    json = {
        "send_type": 1
    }
    response = requests.request("get", url=url, headers=header, json=json)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取账号列表: {response.text}"


def test_accounts_content(get_token):
    url = Domain_path.cicd_domain + Domain_path.subscriptions_path["获取账号信息"]
    header = get_token("tenant_token_header")
    response = requests.request("get", url=url, headers=header)
    assert response.status_code == 200
    assert response.json()["code"] == 0, f"获取账号信息: {response.text}"


if __name__ == "__main__":
    pytest.main(["-vs"])
