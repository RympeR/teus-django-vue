from django.db import models
from users.models import User
from containers.models import UserRequest, UserProposition, Deal
from unixtimestampfield.fields import UnixTimeStampField

class Room(models.Model):

    request_id = models.ForeignKey(
        UserRequest, on_delete=models.CASCADE, related_name='request_chat')
    proposition_id = models.ForeignKey(
        UserProposition, on_delete=models.CASCADE, related_name='proposition_chat')
    date = UnixTimeStampField("Дата создания", auto_now_add=True, null=True, blank=True)
    first_mark = models.BooleanField(default=False)
    second_mark = models.BooleanField(default=False)
    request_user_readed = models.BooleanField(default=False)
    proposition_user_readed = models.BooleanField(default=False)

class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name='Chat room',
                             related_name='chat_room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='user_sender', on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500, null=True, blank=True)
    attachment = models.FileField("Файл", null=True, blank=True)
    date = UnixTimeStampField("Send datetime", auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['-date']
        unique_together = ['date', 'user', 'room']