from django.urls import path
from .views import RegisterView,LoginView,ProfileApiView
 
urlpatterns = [
    path("register/",RegisterView.as_view()),
    path("login/",LoginView.as_view()),
    path("profile/",ProfileApiView.as_view()),
]