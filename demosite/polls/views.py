from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def main(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context)

    return HttpResponse("Hey! polls have been setup.")

def detail(request, question_id):
    return HttpResponse("Yah!, you are in question detail page %s." %question_id)

def results(request, question_id):
    return HttpResponse("Yah!, you are in question results page %s." %question_id)

def vote(request, question_id):
    return HttpResponse("Yah!, you are in question vote page %s." %question_id)
