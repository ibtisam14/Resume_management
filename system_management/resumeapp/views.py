from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.conf import settings
from .models import Resume
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ResumeSerializer, ResumeReviewSerializer
from account.serializers import RegisterSerializer, CustomTokenObtainPairSerializer


# Resume Submit API
class ResumeSubmitView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=ResumeSerializer,
        manual_parameters=[]
    )
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'status': 201, 'message': 'Resume submitted'}, status=201)
        return Response({'status': 400, 'message': 'Submission failed', 'errors': serializer.errors}, status=400)

class ResumeReviewView(APIView):
    permission_classes = [IsAuthenticated]  # User must be authenticated

    @swagger_auto_schema(request_body=ResumeReviewSerializer)
    def post(self, request, resume_id):
        # Allow only users where is_admin=True (custom field on user model)
        if not getattr(request.user, 'is_admin', False):
            raise PermissionDenied("Only admins are allowed to review resumes.")

        try:
            resume = Resume.objects.get(id=resume_id)
        except Resume.DoesNotExist:
            return Response({'status': 404, 'error': 'Resume not found'}, status=404)

        status_choice = request.data.get('status', '').upper()
        if status_choice not in ['ACCEPTED', 'REJECTED']:
            return Response({'status': 400, 'error': 'Invalid status'}, status=400)

        resume.status = status_choice
        resume.save()

        # Send review result via email
        user_email = resume.user.email
        user_name = resume.user.username

        html_content = render_to_string('email_templates/resume_status.html', {
            'username': user_name,
            'status': status_choice,
        })

        text_content = f"Dear {user_name},\n\nYour resume has been {status_choice}.\n\nRegards,\nRecruitment Team"

        email = EmailMultiAlternatives(
            subject='Resume Review Result',
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

        return Response({'status': 200, 'message': f'Resume {status_choice.lower()}'})
