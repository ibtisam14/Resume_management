from django.urls import path
from .views import ResumeSubmitView, ResumeReviewView

urlpatterns = [
    path('submit/', ResumeSubmitView.as_view(), name='resume-submit'),
    path('review/<int:resume_id>/', ResumeReviewView.as_view(), name='resume-review'),
]
