from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html') 
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse('<h1>This is an Item view</h1>')

def detail_view(request, item_id):
  item = Item.objects.get(pk=item_id)
  context = {
    'item': item,
  }
  # return HttpResponse("This is item no/id: %s" % item_id)
  return render(request, 'food/detail.html', context)