from . models import Post
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return HttpResponse("index")


@api_view(['GET'])
def PostListView(request):
    posts = Post.objects.all()
    serializer = BlogSerializer(posts, many = True)
    
    return Response(serializer.data)
    

class PostDetailView(DeleteView):
    queryset = Post.Published.all()
    


def post_detail(request, id):
    post = get_object_or_404(Post, id = id, status = Post.Status.PUBLISHED)
    # try:
    #     post = Post.Published.get(id = id) 
    # except:
    #     raise Http404("No Post Found!")
    context = {
        'post' : post,
    }
    return JsonResponse(context)
    
