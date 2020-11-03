from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# def questionpage(request):
#     return render(request,'question/questionpage.html')

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'question/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(pk=question_id)
        question_pk = request.POST.get('question_pk')

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        

        return HttpResponse("You're voting on 1 question %s." % selected_choice )

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list }
    return render(request, 'question/index.html', context)


def indx(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'question/indx.html', {'question': question})