from django.db import models
from django.contrib.auth.models import User
import os
class User(models.Model):
    user_name = models.CharField(max_length=50, help_text='Enter the user name')
    user_image = models.ImageField(upload_to='images/user', null=True, blank=True)
    user_image2 = models.BinaryField(null=True, blank=True, help_text='Image of user face')
class History(models.Model):
    # View the history of door access
    incident_id = models.AutoField(primary_key=True, help_text='Unique ID for this particular incident')
    door_id = models.ForeignKey('Door', on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to ='images/history', null=True, blank=True)
    image_2 = models.BinaryField(null=True, blank=True, help_text='The image from door device')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']
    def __str__(self):
        return f'{self.incident_id} ({self.door_id.position})'

class Door(models.Model):
    # The door to be accessed
    door_id = models.AutoField(primary_key=True, help_text='Unique ID for this particular door')
    position = models.CharField(max_length=50)

    class Meta:
        ordering = ['door_id']

    def __str__(self):
        return self.position
class Face(models.Model):
    # The face of the user, raw idea. Not complete yet.
    face_id = models.AutoField(primary_key=True, help_text='Unique ID for this particular face')
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'images/face', null=True, blank=True)
    image_2 = models.BinaryField(null=True, blank=True, help_text='Image of user face')

    class Meta:
        ordering = ['face_id']
    
    def __str__(self):
        return f'{self.face_id} ({self.user_id.username})'

