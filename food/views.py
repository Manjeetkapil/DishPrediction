from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post
# Create your views here.
import requests

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')

# @csrf_protect
# def upload(request):
#     img = request.GET['submit']
#     return render(request,'result.html',{'img':img},content_type='application/xhtml+xml')
def index(request):
    MEDIA_URL = '/home/manjeet/django/dish/media/'
    urls_list = [MEDIA_URL + image_path for image_path in Post.objects.values_list('foodimage', flat=True)]
    print(urls_list)
    api_key = 'acc_26d9c07fbcb2472'
    api_secret = 'ad2cffbb1101269a0203b25cf0a59c55'
    image_path = urls_list[-1]
    print(image_path)
    response = requests.post('https://api.imagga.com/v2/tags',auth=(api_key, api_secret),files={'image': open(image_path, 'rb')})
    print(response.json())
    results = response.json()
    result = results["result"]["tags"]
    print(result)
    return render(request,'result.html',{'result':result})