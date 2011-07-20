from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    published_date = models.DateTimeField(auto_now_add = datetime.datetime.now())
    text = models.TextField()
    author = models.ForeignKey(User)
    published = models.BooleanField()

    def __unicode__(self):
        return self.title    

    def publicado_hoy(self):
        return self.fecha.date() == datetime.date.today()
