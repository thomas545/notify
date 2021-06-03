from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='rest_login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
]
