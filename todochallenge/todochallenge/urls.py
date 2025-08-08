from django.urls import (
    include,
    path
)
from todochallenge.admin import admin_site
from users.api.logout import LogoutView
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin_site.urls),
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/', include('tasks.urls'))
]
