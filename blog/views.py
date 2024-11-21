from . models import Post, Ticket
from .forms import TicketForm
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DeleteView
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
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
    

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            ticket_obj.name = form.cleaned_data['name']
            ticket_obj.email = form.cleaned_data['email']
            ticket_obj.message = form.cleaned_data['message']
            ticket_obj.subject = form.cleaned_data['subject']
            ticket_obj.phone = form.cleaned_data['phone']
            ticket_obj.save()
            return render(request, 'forms/success.html', {
                'message': 'Ticket Created!',
                'redirect_url': reverse('blog:ticket')
            })
        
        # when form is not valid:
        return render(request, 'forms/success.html', {
                'message': 'Form is not valid!',
                'redirect_url': reverse('blog:ticket')
            })
    else:
        form = TicketForm()
        return render(request, 'forms/ticket.html', {'form': form})
