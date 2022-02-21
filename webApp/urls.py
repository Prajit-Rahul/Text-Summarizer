from django.urls import path
from webApp.views import HomeView

urlpatterns = [
    path('', HomeView.as_view() ,name = 'home')
]
