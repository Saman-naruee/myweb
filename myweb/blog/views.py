from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DeleteView


# Create your views here.

def index(request):
    return HttpResponse("index")


class PostListView(ListView):
    # model = Post
    context_object_name = 'posts'
    queryset = Post.Published.all()
    paginate_by = 3
    template_name = 'blog/list.html'
    

class PostDetailView(DeleteView):
    queryset = Post.Published.all()
    template_name = "blog/detail.html"


def post_detail(request, id):
    post = get_object_or_404(Post, id = id, status = Post.Status.PUBLISHED)
    # try:
    #     post = Post.Published.get(id = id) 
    # except:
    #     raise Http404("No Post Found!")
    context = {
        'post' : post,
    }
    return render(request, "blog/detail.html", context)
    
