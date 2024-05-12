from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Post

# Create your views here.

def index(request):
    return HttpResponse("index")

def post_list(request):
    posts = Post.Published.all()
    context = {
        'posts' : posts,
    }
    return render(request, "blog/list.html", context)
    

def post_detail(request, id):
    try:
        posts = Post.Published.get(id = id) 
    except:
        raise Http404("No Post Found!")
    
    context = {
        'posts' : posts,
    }
    return render(request, "blog/detail.html", context)
    
    