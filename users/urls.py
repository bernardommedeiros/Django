from django.urls import path
# view existente no django para log-in com verificador de senha e toda a lógica 
from django.contrib.auth import views as authentication

urlpatterns = [
    path('login', authentication.views.LoginView.as_view(template_name='users/login.html'), name='login'),

]

