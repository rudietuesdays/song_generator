from __future__ import unicode_literals
from django.db import models
# from django.forms import ModelForm

# Create your models here.

class SongManager(models.Manager):
    def validate(self, postData):
        messages = []
        flag = False

        if not postData['genre'] or not postData['subj'] or not  postData['pronouns']:
            flag = True
            messages.append('Please fill in all fields !')

        if not flag:
            song = Song.objects.create(genre=postData['genre'], subj=postData['subj'], pronouns=postData['pronouns'])

            return(True, song)

        else:
            return(False, messages)

class Song(models.Model):
    genre = models.CharField(max_length=45)
    subj = models.CharField(max_length=45)
    pronouns = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()

# class Mood(models.Model):
    # def moodPicker(self, request):
    #     mood = request.POST['subj']
    #     if mood == 'happy':
    #
    #         return True
