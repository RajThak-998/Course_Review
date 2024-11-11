# views.py
from django.shortcuts import render, get_object_or_404
from reviews.models import Participant, Assignment, Review
from django.http import HttpResponse
import csv

def home(request):
    return render(request, 'home.html')

def submit_review(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    reviewer = request.user.participant  # Assuming user is linked to Participant

    if Review.objects.filter(reviewer=reviewer).count() >= 3:
        return render(request, 'error.html', {'message': 'You have already reviewed 3 assignments'})

    if Review.objects.filter(assignment=assignment).count() >= 5:
        return render(request, 'error.html', {'message': 'This assignment has already received 5 reviews'})

    if request.method == 'POST':
        content = request.POST['content']
        Review.objects.create(reviewer=reviewer, assignment=assignment, content=content)
        return render(request, 'success.html', {'message': 'Review submitted successfully'})

    return render(request, 'submit_review.html', {'assignment': assignment})

def analytics_view(request):
    participants = Participant.objects.all()
    data = []

    for participant in participants:
        given_reviews = participant.given_reviews.count()
        received_reviews = Review.objects.filter(assignment__participant=participant).count()
        data.append({
            'participant': participant.name,
            'given_reviews': given_reviews,
            'received_reviews': received_reviews,
        })

    return render(request, 'analytics.html', {'data': data})


def download_analytics(request):
    participants = Participant.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="analytics.csv"'

    writer = csv.writer(response)
    writer.writerow(['Participant', 'Given Reviews', 'Received Reviews'])

    for participant in participants:
        given_reviews = participant.given_reviews.count()
        received_reviews = Review.objects.filter(assignment__participant=participant).count()
        writer.writerow([participant.name, given_reviews, received_reviews])

    return response