
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="EduFlux Backend APIs",
      default_version='v1',
      description="This is the API documentation for EduFlux LMS project APIs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vishnuvichuz2019@gmail.com"),
      license=openapi.License(name="ESD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     
     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('admin/', admin.site.urls),
     path("api/v1/", include ("api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
