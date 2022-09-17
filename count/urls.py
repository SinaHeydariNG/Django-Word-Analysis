
from django.urls import path 
from . import views
app_name = 'count'
urlpatterns = [
    path('' , views.count , name='main')
]