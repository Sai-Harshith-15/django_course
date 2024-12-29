from django.urls import path
from .views import index, item

urlpatterns = [
    path('', index, name='index'),
    path('item/', item, name='item'),
]
