from django.urls import path
from .views import index, waiting

urlpatterns = [
    path('', index),
    path('', waiting),

]
