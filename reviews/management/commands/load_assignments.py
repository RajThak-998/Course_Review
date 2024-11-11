import pandas as pd
from django.core.management.base import BaseCommand
from reviews.models import Participant, Assignment

class Command(BaseCommand):
    help = 'Load participant assignments from a CSV file'

    def handle(self, *args, **kwargs):
        # Load data from CSV file
        df = pd.read_csv('/home/rajdevthakur/Documents/Devlopement/06_Django/course_review/result.csv')  # Update the path to your file
        
        for _, row in df.iterrows():
            participant, created = Participant.objects.get_or_create(uid=row['UID'], defaults={'name': row['Name']})
            Assignment.objects.create(participant=participant, content=row['Assignment'])
        
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))