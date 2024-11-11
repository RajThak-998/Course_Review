# reviews/admin.py
from django.contrib import admin
from .models import Participant, Assignment, Review

admin.site.register(Participant)
admin.site.register(Assignment)
admin.site.register(Review)
