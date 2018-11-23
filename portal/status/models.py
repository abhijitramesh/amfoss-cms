from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class thread(models.Model):
    name = models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.name

class status(models.Model):
    date = models.DateTimeField(auto_now=True)
    thread = models.ForeignKey(thread, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=True, blank=True)
    status = RichTextField(max_length=300, null=True)

    class Meta:
        verbose_name_plural = "Status Updates"
        verbose_name = "Status Update"

    def __str__(self):
        return self.author.username