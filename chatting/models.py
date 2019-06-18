from django.db import models
from useraction.models import User
# Create your models here.

class ChattingMessage(models.Model):
    send_side = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_message_side')
    recv_side = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recv_message_side')
    message = models.TextField(default='', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'message_' + self.send_side.username + "_send_to_" + self.recv_side.username
