from zeep import Client
from requests import Session
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from zeep.wsse.username import UsernameToken


def send_sms(phone, text):
    session = Session()
    session.auth = HTTPBasicAuth('Teus', 'teus_container')
    session.verify = False
    transport = Transport(session=session)
    client = Client(
        'http://turbosms.in.ua/api/wsdl.html',
        transport=transport,
        wsse=UsernameToken('Teus', 'teus_container')
    )
    result = client.service.Auth(
        login="Teus",
        password='teus_container',
    )
    print(f'{result} ->auth')
    phone = '+' + str(phone)
    result = client.service.SendSMS(
        sender="TEUs",
        destination=phone,
        text='Code ' + str(text),
    )
    print(f'{result} ->sendsms')
