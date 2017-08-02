
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Experiment,XpConfig,PastInteraction
# ...
import json

from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required#(login_url='/accounts/login/')
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/ng/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'ng/index.html'
    context_object_name = 'latest_experiment_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Experiment.objects.all()

#@login_required#(login_url='/accounts/login/')


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/ng/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Experiment
    template_name = 'ng/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Experiment.objects.filter()


class ResultsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/ng/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Experiment
    template_name = 'ng/results.html'



@login_required(login_url='/ng/accounts/login/')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ng/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ng:results', args=(question.id,)))


@login_required(login_url='/ng/accounts/login/')
def testdet(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    return render(request, 'ng/detail.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })


@login_required(login_url='/ng/accounts/login/')
def continue_xp(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    experiment.continue_xp(steps=1)
    #raise IOError(experiment)
    #experiment.update_results()
    experiment.save()
    return render(request, 'ng/detail.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })

@login_required(login_url='/ng/accounts/login/')
def result_srtheo(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    experiment.update_results()
    experiment.save()
    return render(request, 'ng/results.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })




@login_required(login_url='/ng/accounts/login/')
def result_hearer(request, xp_uuid, meaning):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    currentgame_json = experiment.get_currentgame_json()
    currentgame_json.update({'mh':int(meaning)})
    ms = currentgame_json['ms']
    w = currentgame_json['w']
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=ms,word=w,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='hearer',experiment=experiment)
    experiment.save()
    past_interaction.save()
    return render(request, 'ng/global.html', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"hearer",
            'context':"result"
        })

@login_required(login_url='/ng/accounts/login/')
def result_speaker(request, xp_uuid, meaning, word):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    currentgame_json = experiment.get_currentgame_json()
    ms = int(meaning)
    w = word
    currentgame_json.update({'ms':ms,'w':w})
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=ms,word=w,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='speaker',experiment=experiment)
    experiment.save()
    past_interaction.save()
    #return render(request, 'ng/results_new.html', {
    #        'experiment': experiment,
    #        'bool_succ': bool_succ,
    #    })
    return render(request, 'ng/global.html', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"speaker",
            'context':"result"

        })



@login_required(login_url='/ng/accounts/login/')
def new_experiment(request):
    experiment = Experiment.get_new_xp()
    experiment.save()
    return render(request, 'ng/global.html', {
            'experiment': experiment,
            'textid': "new_xp",
            'context':"new_xp"
        })

@login_required(login_url='/ng/accounts/login/')
def continue_userxp(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    try:
        experiment.continue_xp(steps=1)
        experiment.save()
        return render(request, 'ng/global.html', {
                'experiment': experiment,
                'textid': "not_involved",
            })

    except IOError as e:
        if str(e) == 'User intervention needed':
            currentgame_json = experiment.get_currentgame_json()
            experiment.save()
            sp_id = currentgame_json['speaker_id']
            hr_id = currentgame_json['hearer_id']
            experiment.update_meanings()
            experiment.update_words()
            if sp_id == experiment.get_user_agent_uuid():
                return render(request, 'ng/global.html', {
                    'experiment': experiment,
                    'role':"speaker",
                    'context':"question"
                    })
            elif hr_id == experiment.get_user_agent_uuid():
                return render(request, 'ng/global.html', {
                    'experiment': experiment,
                    'word': currentgame_json['w'],
                    'role':"hearer",
                    'context':"question"
                    })
            else:
                raise
        else:
            raise

