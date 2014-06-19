from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FeedbackModel(models.Model):
    user = models.ForeignKey(User,related_name="user_feedback_FK")
    subject = models.CharField("Subject", max_length=16)
    body = models.CharField("Body", max_length=200)
    email = models.CharField("Email", max_length=32)
    