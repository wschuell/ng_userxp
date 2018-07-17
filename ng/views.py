
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from django.contrib.auth.models import User

from .models import UserNG,Experiment,XpConfig,PastInteraction,Score
# ...
import json
import uuid

from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from .forms import NameForm

def create_user(request,username='',name='',cookie_id='', lang='fr', code=''):
    user = User.objects.create_user(username=str(username),first_name=str(name),email=str(cookie_id),password=str(username))
    user.save()
    #Extended model of User
    #userNG = UserNG(user = user, lang=str(lang), code=str(code))
    #userNG.save()

def login_user(request,username=''):
    user = authenticate(request, username=username, password=username)
    if user is not None :
        #print("in login")
        #request.session["user"] = user
        login(request, user)

def login_view(request):
    username = 'oug'
    return render(request, 'ng/login.html', {
            'username': username,
        })

@csrf_protect
@login_required(login_url='/ng/login')
def home(request):
    user = request.user
    u = UserNG.get(user=user)
    game_unlocked = u.tuto_played
    if (u.nbr_played < 5):
        multi_unlocked = False
    else :
        multi_unlocked = True
    return render(request, 'ng/home.html', {
    'game_unlocked' : game_unlocked,
    'multi_unlocked' : multi_unlocked,
    'user': u,
    })

def create_and_login(request,username=None,name='',cookie_id=None, lang='fr', code=''):
    if username is None:
        username = name+str(cookie_id)
    if not User.objects.filter(username=username).exists():
        create_user(request,username,name=name,cookie_id=cookie_id)
        login_user(request,username)
        u = UserNG.get(user=request.user)
        u.lang = lang
        u.code = code
        u.save()
    else :
        login_user(request,username)
    #print("in login")
    #request.session["user"] = user
    #return render(request,'ng/index.html',{})

@csrf_protect
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            cookie_id = form.cleaned_data['name_cookie_id']
            lang = form.cleaned_data['lang']
            code = form.cleaned_data['code']
            create_and_login(request=request,name=name,cookie_id=cookie_id, lang=lang, code=code)
            return HttpResponseRedirect('/ng/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'ng/login_name.html', {'form': form})

#@login_required#(login_url='/accounts/login/')
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/ng/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'ng/index.html'
    context_object_name = 'latest_experiment_list'
    def get_queryset(self):
        return Experiment.objects.all()

#@login_required#(login_url='/accounts/login/')


#Story view if user chooses tutorial
@login_required(login_url='/ng/login/')
def story(request) :
	return render(request, 'ng/story.html', {'context':'story', 'userNG': UserNG.get(user=request.user)})


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/ng/login/'
    redirect_field_name = 'redirect_to'
    model = Experiment
    template_name = 'ng/detail.html'
    def get_queryset(self):
        return Experiment.objects.filter()


class ResultsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/ng/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Experiment
    template_name = 'ng/results.html'



@csrf_protect
@login_required(login_url='/ng/login/')
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


@login_required(login_url='/ng/login/')
def testdet(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    return render(request, 'ng/detail.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def continue_xp(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    experiment.continue_xp(steps=1)
    #raise IOError(experiment)
    #experiment.update_results()
    experiment.save()
    return render(request, 'ng/detail.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def result_srtheo(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    experiment.update_results()
    experiment.save()
    return render(request, 'ng/results.html', {
            'experiment': experiment,
            'error_message': "You didn't select a choice.",
        })




@csrf_protect
@login_required(login_url='/ng/login/')
def result_hearer(request, xp_uuid, meaning):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    currentgame_json = experiment.get_currentgame_json()
    if meaning == 'none':
        currentgame_json.update({'mh':None})
    else:
        currentgame_json.update({'mh':int(meaning)})
    ms = currentgame_json['ms']
    w = currentgame_json['w']
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=str(ms),word=w,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='hearer',experiment=experiment)
    experiment.save()
    past_interaction.save()
    return render(request, 'ng/game.html', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"hearer",
            'context':"result"
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def result_speaker(request, xp_uuid, meaning, word):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    currentgame_json = experiment.get_currentgame_json()
    ms = int(meaning)
    w = word
    currentgame_json.update({'ms':ms,'w':w})
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=str(ms),word=w,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='speaker',experiment=experiment)
    experiment.save()
    past_interaction.save()
    #return render(request, 'ng/results_new.html', {
    #        'experiment': experiment,
    #        'bool_succ': bool_succ,
    #    })
    return render(request, 'ng/game.html', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"speaker",
            'context':"result"

        })


@csrf_protect
@login_required(login_url='/ng/login/')
def none(request):
    return None

@csrf_protect
@login_required(login_url='/ng/login/')
def result_inner(request, xp_uuid, bool_succ):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    past_int = experiment.pastinteraction_set.last()
    return render(request, 'ng/game.html', {
            'experiment': experiment,
            'bool_succ': past_int.bool_succ,
            'ms':past_int.meaning,
            'word':past_int.word,
            'mh':past_int.meaning_h,
            'role':past_int.role,
            'username':request.user.username,
            'context' : "result",
        })


@csrf_protect
@login_required(login_url='/ng/login/')
def result_hearer_json(request, xp_uuid, meaning):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    try:
        currentgame_json = experiment.get_currentgame_json()
    except:
        return render(request, 'ng/result.json', {
            'experiment': experiment,
            'bool_succ': experiment.last_bool_succ,
            'role':"hearer",
            'context':"result",
            'ms':experiment.last_ms,
        })
    if meaning == 'none':
        currentgame_json.update({'mh':None})
    else:
        currentgame_json.update({'mh':int(meaning)})
    ms = int(currentgame_json['ms'])
    w = currentgame_json['w']
    experiment.save_currentgame_json(currentgame_json)
    #experiment.add_word_to_user(w)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=str(ms),word=w,meaning_h=str(meaning),bool_succ=bool_succ,time_id=experiment.interaction_counter,role='hearer',experiment=experiment)
    experiment.save()
    past_interaction.save()
    return render(request, 'ng/result.json', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"hearer",
            'context':"result",
            'ms':ms,
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def result_hearer_continue(request, xp_uuid, meaning):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    try:
        currentgame_json = experiment.get_currentgame_json()
    except:
        return render(request, 'ng/game.html', {
            'experiment': experiment,
            'context':"result",
        })
    if meaning == 'none':
        currentgame_json.update({'mh':None})
    else:
        currentgame_json.update({'mh':int(meaning)})
    ms = currentgame_json['ms']
    w = currentgame_json['w']
    experiment.save_currentgame_json(currentgame_json)
    #experiment.add_word_to_user(w)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    past_interaction = PastInteraction(meaning=str(ms),word=w,meaning_h=str(meaning),bool_succ=bool_succ,time_id=experiment.interaction_counter,role='hearer',experiment=experiment)
    experiment.save()
    past_interaction.save()
    return render(request, 'ng/game.html', {
            'experiment': experiment,
            'context':"result",
            'role': "hearer",
            'word':w,
            'last_mh': str(currentgame_json['mh']),
            'last_ms': ms,
            'bool_succ': bool_succ,
            'user':request.user,
            'userNG': UserNG.get(user=request.user),

        })

@csrf_protect
@login_required(login_url='/ng/login/')
def result_speaker_json(request, xp_uuid, meaning, word):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    try:
        currentgame_json = experiment.get_currentgame_json()
    except:
        return render(request, 'ng/result.json', {
            'experiment': experiment,
            'bool_succ': experiment.last_bool_succ,
            'role':"speaker",
            'context':"result",
        })
    ms = int(meaning)
    w = word
    currentgame_json.update({'ms':ms,'w':w})
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    mh = experiment.get_last_mh()
    if mh is None:
        mh = 'none'
    else:
        mh = int(mh)
    past_interaction = PastInteraction(meaning=ms,word=w,meaning_h=mh,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='speaker',experiment=experiment)
    experiment.save()
    past_interaction.save()
    # if experiment.xp_config.xp_cfg_name == 'multiuser':
    #     experiment.exchange_agent(1, 2)
    experiment.save()
    #return render(request, 'ng/results_new.html', {
    #        'experiment': experiment,
    #        'bool_succ': bool_succ,
    #    })
    return render(request, 'ng/result.json', {
            'experiment': experiment,
            'bool_succ': bool_succ,
            'role':"speaker",
            'context':"result",
            'user':request.user,
            'userNG': UserNG.get(user=request.user),
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def result_speaker_continue(request, xp_uuid, meaning, word):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    try:
        currentgame_json = experiment.get_currentgame_json()
    except:
        return render(request, 'ng/game.html', {
            'experiment': experiment,
            'context':"result",
        })
    ms = int(meaning)
    w = word
    currentgame_json.update({'ms':ms,'w':w})
    experiment.save_currentgame_json(currentgame_json)
    experiment.continue_xp()
    bool_succ = experiment.get_last_bool_succ()
    mh = experiment.get_last_mh()
    if mh is None:
        mh = 'none'
    else:
        mh = int(mh)
    past_interaction = PastInteraction(meaning=str(ms),word=w,meaning_h=mh,bool_succ=bool_succ,time_id=experiment.interaction_counter,role='speaker',experiment=experiment)
    experiment.save()
    past_interaction.save()
    # if experiment.xp_config.xp_cfg_name == 'multiuser':
    #     experiment.exchange_agent(1, 2)
    experiment.save()
    #return render(request, 'ng/results_new.html', {
    #        'experiment': experiment,
    #        'bool_succ': bool_succ,
    #    })
    return render(request, 'ng/game.html', {
            'experiment': experiment,
            'context':"result",
            'role': "speaker",
            'word':w,
            'last_mh': mh,
            'last_ms': str(currentgame_json['ms']),
            'bool_succ': bool_succ,
            'user':request.user,
            'userNG': UserNG.get(user=request.user),
        })



@csrf_protect
@login_required(login_url='/ng/login/')
def choose_experiment(request,xp_cfg_name='normal'):
    return render(request, 'ng/global.html', {
            'context':"choose_xp"
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def new_experiment(request,xp_cfg_name='normal'):
    #Test if the user can access this type of game and send them to the home page if not
    user = request.user
    u = UserNG.get(user=user)
    if ((xp_cfg_name == "normal" and not u.tuto_played) or (xp_cfg_name == "multiuser" and u.nbr_played < 5)):
        return HttpResponseRedirect('/')
    else :
        experiment = Experiment.get_new_xp(user=request.user,xp_cfg_name=xp_cfg_name)
        experiment.save()
        return render(request, 'ng/loading_xp.html', {
            'experiment': experiment,
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def test(request):
    experiment = Experiment.get_new_xp()
    experiment.save()
    return render(request, 'ng/test.html', {
            'experiment': experiment,
        })

@csrf_protect
@login_required(login_url='/ng/login/')
def continue_userxp(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    if 0 < experiment.max_interaction <= experiment.interaction_counter:
        # if experiment.xp_config.xp_cfg_name == 'multiuser':
        #     experiment.transfer_agents()
        return score(request, xp_uuid=xp_uuid)
    try:
        experiment.continue_xp(steps=1)
        nb_steps = 1
        try:
            while nb_steps<1000:
                experiment.continue_xp(steps=1)
                nb_steps += 1
            raise IOError('Not skipping more than 1000 steps at a time')
        except Exception as e:
            if str(e) == 'User intervention needed' or str(e) == 'Not skipping more than 1000 steps at a time':
                experiment.last_role = 'skipped'
                experiment.last_nb_skipped = nb_steps
                experiment.last_ms = None
                experiment.last_w = None
                experiment.last_mh = None
                experiment.last_bool_succ = False
                experiment.save()
                #
                bar_width = ((experiment.interaction_counter + 1) / experiment.max_interaction )*100
                return render(request, 'ng/game.html', {
                    'experiment': experiment,
                    'textid': "not_involved",
                    'nb_skipped': nb_steps,
                    'context': 'skipped',
                    'bar_width':bar_width,
                    'user':request.user,
                    'userNG': UserNG.get(user=request.user),

                       })

    except Exception as e:
        if str(e) == 'User intervention needed':
            currentgame_json = experiment.get_currentgame_json()
            experiment.save()
            sp_id = currentgame_json['speaker_id']
            hr_id = currentgame_json['hearer_id']
            # experiment.update_meanings()
            # experiment.update_words()
            bar_width = ((experiment.interaction_counter + 1) / experiment.max_interaction )*100
            if sp_id == experiment.get_user_agent_uuid():
                return render(request, 'ng/game.html', {
                    'experiment': experiment,
                    'role':"speaker",
                    'context':"question",
                    'bar_width':bar_width,
                    'user':request.user,
                    'userNG': UserNG.get(user=request.user),
                    })
            elif hr_id == experiment.get_user_agent_uuid():
                return render(request, 'ng/game.html', {
                    'experiment': experiment,
                    'word': currentgame_json['w'],
                    'role':"hearer",
                    'context':"question",
                    'bar_width':bar_width,
                    'user':request.user,
                    'userNG': UserNG.get(user=request.user),
                    })
            else:
                raise Exception('Exception catch failed, sp_id or hr_id not recognized')
        else:
            print('Exception catch failed:',str(e))
            raise


@csrf_protect
@login_required(login_url='/ng/login/')
def exp_resume(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    return render(request, 'ng/global.html', {
            'experiment': experiment,
            'context':"resume",
            })



@csrf_protect
@login_required(login_url='/ng/login/')
def score(request, xp_uuid):
    experiment = get_object_or_404(Experiment, xp_uuid=xp_uuid)
    if request.user != experiment.user:
        raise ValueError("wrong user")
    request.user.last_name = "test"
    request.user.save()
    try:
        score = Score.objects.get(experiment=experiment)
        score_val = score.score
    except:
        experiment.get_xp()
        srtheo = experiment.xp.graph(method="srtheo")._Y[0][-1]
        score_val = int(srtheo * experiment.meanings.count() * 100)#.all().count()?
        score = Score(experiment=experiment,score=score_val,user=request.user)
        score.save()
    u = UserNG.get(user=request.user)
    if experiment.xp_config.xp_cfg_name == "normal" :
        u.nbr_played =+ 1
        u.save()
    elif experiment.xp_config.xp_cfg_name == "basic" and u.tuto_played == False :
        u.tuto_played = True
        u.save()
    #Test if score exists
    #if not, compute and store object
    #get value
    return render(request, 'ng/story.html', {
            'experiment': experiment,
            'score':score_val,
            'context':"end",
            'user':request.user,
            'userNG': UserNG.get(user=request.user),
            })
