from django.db import models
from users.models import User
from containers.models import UserRequest, UserProposition
from unixtimestampfield.fields import UnixTimeStampField
from info.models import City, Container, Line

class Room(models.Model):

    request_id = models.ForeignKey(
        UserRequest, on_delete=models.CASCADE, related_name='request_chat')
    proposition_id = models.ForeignKey(
        UserProposition, on_delete=models.CASCADE, related_name='proposition_chat')
    date = UnixTimeStampField("Дата создания", auto_now_add=True, null=True, blank=True)
    first_mark = models.BooleanField(default=False)
    second_mark = models.BooleanField(default=False)
    request_user_readed = models.BooleanField(default=True)
    proposition_user_readed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pk}-p-{self.proposition_id.user}-u-{self.request_id.user}'
class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name='Chat room',
                             related_name='chat_room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='user_sender', on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500, null=True, blank=True)
    attachment = models.FileField("Файл", null=True, blank=True)
    date = UnixTimeStampField("Send datetime", auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.pk}-p-{self.room}-u-{self.user}'
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['-date']
        unique_together = ['date', 'user', 'room']

class Deal(models.Model):
    user_request = models.ForeignKey(User, related_name='deal_user_request', on_delete=models.CASCADE)
    user_proposition = models.ForeignKey(User, related_name='deal_user_proposition', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_deal', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(verbose_name='Кол-во')
    city = models.ForeignKey(City, related_name='city_deal', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='line_deal', on_delete=models.CASCADE)
    container = models.ForeignKey(Container, related_name='container_deal', on_delete=models.CASCADE)
    handshake_time = UnixTimeStampField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.pk}-p-{self.user_request}-u-{self.user_proposition}'
    class Meta:
        ordering = ['-handshake_time']
