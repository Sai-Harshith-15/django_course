from django.urls import path
from .views import index, item, detail_view

urlpatterns = [
  #/food
  path('', index, name='index'),
  #/food/1
  path('<int:item_id>/', detail_view, name='detail_view'),
  
  path('item/', item, name='item'),
]
