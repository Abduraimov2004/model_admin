from django.urls import path
from .views import waiting
urlpatterns = [
    path('', waiting),

]