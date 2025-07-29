from django.urls import path
from .views import ResumeSubmitView, ResumeReviewView

urlpatterns = [
    path('resume/submit/', ResumeSubmitView.as_view(), name='resume-submit'),
    path('resume/review/<int:resume_id>/', ResumeReviewView.as_view(), name='resume-review'),
]
