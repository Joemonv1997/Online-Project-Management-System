from django.urls import path
from .views import loginpage, logoutpage, registerpage
urlpatterns = [
    path('login',loginpage,name="Login"),
    path('logout',logoutpage,name="Logout"),
    path('register',registerpage,name="Register"),
]