from django.urls import path
from .views import index

app_name = 'frontend'
# the reason app_name is assigned is cause django needs to know that the urls.py file belongs to the frontend app

# name if one redirects to 'frontend:hello' it would be redirected index if its name is hello

urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create',index),
    path('room/<str:roomCode>', index)
]
