from onesignal import Client
import onesignal
from django.utils.html import strip_tags
import logging
logger = logging.getLogger('django')
onesignal_client = Client(
    user_auth_key="NTQyZmY5NjctYmNjMC00OTU3LTlmMDgtZmUyZjU3ZjM2ZDgw",
    app_auth_key='YTFlMDc1NWItNTA0Yy00ZWE3LTkzOTEtNzdkYTliZDY4MmY3',
    app_id="3d278d7c-b7db-4698-8066-7b1ec919d19c"
)

def send_push(title_ru, text_ru, user_id, push_data=None):
    def push_replace(a):
        return strip_tags(str(a)).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    data = {
        "headings": {"ru": str(title_ru), 
            "en":str(title_ru)},
        "contents": {
            "ru": push_replace(text_ru),
            "en": push_replace(text_ru)
        },
        "include_player_ids": [str(user_id)],
    }
    data['mutable_content'] = {"content_available" : "1"}
    if push_data:
        data['data'] = push_data

    # create a notificatio
    logger.warning(user_id)
    notification = onesignal.Notification(post_body=data)
    # send notification, it will return a response
    # logging.warning('createdd notification')
    onesignal_response = onesignal_client.send_notification(notification)
    logger.warning(onesignal_response.status_code)
    logger.warning(onesignal_response.json())
    # logging.warning('Sended notification')
