from django.urls import path

from .views import *


urlpatterns = [
    path('', display_all_articles),
]
