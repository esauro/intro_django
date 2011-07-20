from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200)
	published_date = models.DateTimeField(auto_now_add = datetime.datetime.now())
	text = models.TextField()
