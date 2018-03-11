from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# default use a template <appname>/<modelname>_detail.html
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # ListView automatically generated context variable "question_list",
    # override with context_object_name
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # returns a queryset containing Questions whose pub_date is less than or equal to timezone.now.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# each generic needs know model,
# capture primary key value called 'pk' in the URL,
# default use a template <appname>/<modelname>_detail.html
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectd_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question,
                     'error_message': "You didn't select a choice"})
    else:
        selectd_choice.votes += 1
        selectd_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))

