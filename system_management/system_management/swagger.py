from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Resume Management System",
        default_version='Beta',
        description="API documentation using Swagger UI",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mh40880@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
