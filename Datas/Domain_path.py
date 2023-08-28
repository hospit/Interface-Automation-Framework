
cicd_domain = ""

account_id = ""
# message_id = ""  # 由创建文章获取
subscriptions_path = {
    "转存图片": "/open-apis/subscriptions/v1/images/transfer",
    "创建订阅号文章": f"/open-apis/subscriptions/v1/accounts/{account_id}/messages",
    "发送订阅号文章": f"/open-apis/subscriptions/v1/accounts/{account_id}/messages/:message_id/send",
    "获取订阅号消息（文章）列表": f"/open-apis/subscriptions/v1/accounts/{account_id}/messages",
    "获取订阅号消息（文章）内容": f"/open-apis/subscriptions/v1/accounts/{account_id}/messages/:message_id",
    "获取账号列表": "/open-apis/subscriptions/v1/accounts",
    "获取账号信息": f"/open-apis/subscriptions/v1/accounts/{account_id}"
}

calendars_path = {
    "创建日历": "/open-apis/calendar/v4/calendars",
    "获取主日历": "/open-apis/calendar/v4/calendars/primary",
    "获取日历": "/open-apis/calendar/v4/calendars/:calendar_id",
    "获取日历列表": "/open-apis/calendar/v4/calendars",
    "更新日历": "/open-apis/calendar/v4/calendars/:calendar_id",
    "搜索日历": "/open-apis/calendar/v4/calendars/search",
    "订阅日历": "/open-apis/calendar/v4/calendars/:calendar_id/subscribe",
    "取消订阅日历": "/open-apis/calendar/v4/calendars/:calendar_id/unsubscribe",
    "订阅日历变更事件": "/open-apis/calendar/v4/calendars/subscription",
    "取消订阅日历变更事件": "/open-apis/calendar/v4/calendars/unsubscription"
}

events_path = {
    "创建日程": "/open-apis/calendar/v4/calendars/:calendar_id/events",
    "删除日程": "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id",
    "获取日程": "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id",
    "更新日程": "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id",
    "搜索日程": "/open-apis/calendar/v4/calendars/:calendar_id/events/search",
    "订阅日程变更事件": "/open-apis/calendar/v4/calendars/:calendar_id/events/subscription",
    "获取日程列表": "/open-apis/calendar/v4/calendars/:calendar_id/events"
}















