from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Question, Choice

#GEt questions and display them

def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific qns and choices

def detial(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question not found')
    return render(request, 'polls/results.html', {'question': question})

# get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question})
