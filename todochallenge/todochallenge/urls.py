from django.urls import (
    include,
    path
)
from todochallenge.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('api/v1/', include('tasks.urls')),
]
