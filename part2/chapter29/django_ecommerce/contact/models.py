from django.db import models
import datetime

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    topic = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)

    def __unicode__(self):
        return self.email

class Meta:
    ordering = ['-timestmap']
