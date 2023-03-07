from django.urls import path
from users.views import login, logout, profile, registration

urlpatterns = [
    path('login/', login, name='login_user'),
    path('logout/', logout, name='logout'),
    path('login/profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
]
