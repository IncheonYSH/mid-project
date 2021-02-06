from django.urls import path
from django.urls import include
from accounts import views
from .views import signup

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]