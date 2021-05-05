import onesignal as onesignal_sdk
from django.utils.html import strip_tags

onesignal_client = onesignal_sdk.Client(
    user_auth_key="NTQyZmY5NjctYmNjMC00OTU3LTlmMDgtZmUyZjU3ZjM2ZDgw",
    rest_api_key='YTFlMDc1NWItNTA0Yy00ZWE3LTkzOTEtNzdkYTliZDY4MmY3',
    app_id="3d278d7c-b7db-4698-8066-7b1ec919d19c"
)

def send_push(title_ru, text_ru, user_id, push_data=None):
    def push_replace(a):
        return strip_tags(str(a)).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    data = {
        "headings": {"ru": str(title_ru)},
        "contents": {
            "ru": push_replace(text_ru),
        },
        "include_player_ids": [str(user_id)],
    }
    if push_data:
        data['data'] = push_data

    # create a notification
    notification = onesignal_sdk.Notification(post_body=data)

    # send notification, it will return a response
    onesignal_client.send_notification(notification)
