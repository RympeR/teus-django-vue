from zeep import Client
from requests import Session
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from zeep.wsse.username import UsernameToken
import onesignal as onesignal_sdk
import datetime
import os
import re
import random
import string

import requests
import hashlib
import json
from django.core.validators import validate_email
import time
from django.utils.html import strip_tags

onesignal_client = onesignal_sdk.Client(
    user_auth_key="NTQyZmY5NjctYmNjMC00OTU3LTlmMDgtZmUyZjU3ZjM2ZDgw",
    app_auth_key="YTZmNzZjNTItMDQ1Yy00MjMxLWE3ZjMtZmM2ZDc5OTg2N2U5",
    app_id="02fba9f1-d74a-4f01-8310-9c96efa918ef"
)

def set_phone(phone):
    phone = str(phone)
    if phone and type(phone) is not int:
        phone = re.sub("\D", '', phone)

        if len(phone) == 9:
            phone = '380' + phone

        if phone[:1] == '0':
            phone = '38' + phone
        if phone[:1] == '8':
            phone = '3' + phone

        if len(phone) == 12:
            return int(phone)
    return None


def set_email(email):
    try:
        validate_email(email)
        return email
    except Exception:
        return None

def send_sms(phone, text):
    session = Session()
    session.auth = HTTPBasicAuth('33M2etra', 'docent6495995')
    session.verify = False
    transport = Transport(session=session)
    client = Client(
        'http://turbosms.in.ua/api/wsdl.html',
        transport=transport,
        wsse=UsernameToken('33M2etra', 'docent6495995')
    )
    result = client.service.Auth(
        login="33M2etra",
        password='docent6495995',
    )
    print(result)
    result = client.service.SendSMS(
        sender="33m2",
        destination=phone,
        text=text,
    )
    print(result)

def send_push(title_ru, text_ru, title_ua, text_ua, image, player_id, push_data=None):
    def push_replace(a):
        return strip_tags(str(a)).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    data = {
        "headings": {"en": str(title_ru), "ru": str(title_ru), "ua": str(title_ua)},
        "contents": {
            "en": push_replace(text_ru),
            "ru": push_replace(text_ru),
            "ua": push_replace(text_ua)
        },
        "include_player_ids": [str(player_id)],
    }
    if image:
        data["ios_attachments"] = {'id': image}
        data["big_picture"] = image
        data["data"] = {
            "ios_attachments": {'id': image},
            "big_picture": image,
        }
        data["attachments"] = {
            "ios_attachments": {'id': image},
            "big_picture": image,
        }

    if push_data:
        if image:
            data['data'] += push_data
        else:
            data['data'] = push_data

    # create a notification
    notification = onesignal_sdk.Notification(post_body=data)

    # send notification, it will return a response
    onesignal_client.send_notification(notification)