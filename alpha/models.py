from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Members(models.Model):
    email = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    signup_date = models.DateTimeField(auto_now=True)
    contents = models.TextField(max_length=300)

class Thread(models.Model):
    owner = models.IntegerField(max_length = 50)
    topic = models.CharField(max_length=500)
    title = models.CharField(max_length = 500)
    post_date = models.DateTimeField(auto_now = True)

class Replies(models.Model):
    owner = models.IntegerField(max_length = 50)
    thread = models.IntegerField(max_length = 50)
    content = models.CharField(max_length = 500)
    preference = models.IntegerField(max_length = 1000)
    post_date = models.DateTimeField(auto_now = True)
    parent_id = models.IntegerField(max_length = 50)

class Celeb_info(models.Model):
    owner = models.IntegerField(max_length = 50)
    name = models.CharField(max_length=100)
    birth = models.DateTimeField(auto_now = False)
    group = models.CharField(max_length = 500)
    job = models.CharField(max_length = 500)
    school = models.CharField(max_length = 500)

class Celeb_info_career(models.Model):
    owner = models.IntegerField(max_length = 50)
    _from = models.DateTimeField(auto_now = False)
    _to = models.DateTimeField(auto_now = False)
    award = models.CharField(max_length = 500)
