from django.shortcuts import render
from django.http import HttpResponse
from . models import Question

# def index(request : HttpResponse) -> HttpResponse :
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request : HttpResponse) -> HttpResponse :
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request : HttpResponse, question_id : int):
    return HttpResponse(f"You're looking at question {question_id}"  )


def results(request : HttpResponse, question_id : int) -> HttpResponse :
    response = "You're looking at the results of question ."
    return HttpResponse(response + str(question_id))


def vote(request : HttpResponse, question_id : int) -> HttpResponse :
    return HttpResponse(f"You're voting on question {question_id}.")