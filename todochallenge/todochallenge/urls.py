from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    include,
    path
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from todochallenge.admin import admin_site
from users.api.logout import LogoutView
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin_site.urls),
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', include('tasks.urls')),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/v1/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
