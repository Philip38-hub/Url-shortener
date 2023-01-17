from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Url

def index(request):
    return render(request, 'index.html')

# Create your views here.

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = link, uuid = uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_detail = Url.objects.get(uid=pk)
    return redirect('https://'+url_detail.link)
    
