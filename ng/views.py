
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



class IndexView(generic.ListView):
    template_name = 'ng/index.html'
    context_object_name = 'latest_experiment_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Experiment.objects.all()

def get_new_xp():
    xp_cfg = {
        "step": 1,
        "pop_cfg": {
        "voc_cfg": {
            "voc_type": "2dictdict"
        },
        'agent_init_cfg':{
            'agent_init_type':'oneuser_noninteractive',
            },
        "strat_cfg": {
            "vu_cfg": {
            "vu_type": "minimalsynonly"
            },
            "success_cfg": {
            "success_type": "global"
            },
            "strat_type": "naive"
        },
        "nbagent": 7,
        "env_cfg": {
            "env_type": "simple_realwords",
            "M": 5,
            "W": 6
        },
        "interact_cfg": {
            "interact_type": "speakerschoice"
            }
            }
            }
    xp_conf_obj = XpConfig(xp_config=json.dumps(xp_cfg))
    xp_conf_obj.save()
    xp = Experiment(xp_config=xp_conf_obj)
    xp.get_xp()
    xp.save()
    return xp

class DetailView(generic.DetailView):
    model = Experiment
    template_name = 'ng/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Experiment.objects.filter()


class ResultsView(generic.DetailView):
    model = Experiment
    template_name = 'ng/results.html'



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


def testdet(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    return render(request, 'ng/detail.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })


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

def result_srtheo(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    experiment.update_results()
    experiment.save()
    return render(request, 'ng/results.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })




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




def new_experiment(request):
    experiment = get_new_xp()
    experiment.save()
    return render(request, 'ng/global.html', {
            'experiment': experiment,
            'error_message': "This experiment has not started yet.",
            'context':"new_xp"
        })

def continue_userxp(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    try:
        experiment.continue_xp(steps=1)
        experiment.save()
        return render(request, 'ng/global.html', {
                'experiment': experiment,
                'error_message': "You were not involved in this interaction.",
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

