from django.urls import path
from .views import (
    RegisterView,
    ResumeSubmitView,
    ResumeReviewView,
    CustomTokenObtainPairView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('resume/submit/', ResumeSubmitView.as_view(), name='resume-submit'),
    path('resume/review/<int:resume_id>/', ResumeReviewView.as_view(), name='resume-review'),
]
