from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

class Assignment(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    content = models.TextField()

class Review(models.Model):
    reviewer = models.ForeignKey(Participant, related_name='given_reviews', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)