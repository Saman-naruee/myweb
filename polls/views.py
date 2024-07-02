from django.shortcuts import render
from django.http import HttpResponse
from . models import Question
from django.template import loader

# def index(request : HttpResponse) -> HttpResponse :
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request : HttpResponse) -> HttpResponse :
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request : HttpResponse, question_id : int):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return HttpResponse('Not Found', status = 404)
    return render(
        request=request,
        template_name='polls/detail.html',
        context={
            'question':question
        },
            
        
    )
    


def results(request : HttpResponse, question_id : int) -> HttpResponse :
    response = "You're looking at the results of question ."
    return HttpResponse(response + str(question_id))


def vote(request : HttpResponse, question_id : int) -> HttpResponse :
    return HttpResponse(f"You're voting on question {question_id}.")

