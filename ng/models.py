# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.timezone import now

import naminggamesal as ngal

# Create your models here.

import json
import pickle
import random
import datetime
import copy

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
            "strat_type": "naive",
            "allow_idk":True,
        },
        "nbagent": 5,
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

null_date = None
MEANING_LIST = list(range(13))

#extended User class
class UserNG(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    lang = models.CharField(max_length=3, default="en")
    #ID for certain types of Users
    code = models.CharField(max_length=100, null=True, blank= True, default='')
    #Number of games played, used as condition for unlocking game modes
    tuto_played = models.BooleanField(default=False)
    nbr_played = models.IntegerField(default=0)
    nbr_won = models.IntegerField(default=0)
    use_matomo = models.BooleanField(default=True)
    prolific_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Has the user seen the informations displayed after 3 games ?
    q_seen = models.BooleanField(default=False)
    q_seen_at = models.DateTimeField(blank=True,null=True,default=null_date)

    #Has the user already filled the form ?
    q_filled = models.BooleanField(default=False)

    #Questions
    q1 =  models.BooleanField(default=False)
    q2 =  models.BooleanField(default=False)
    q3 =  models.BooleanField(default=False)
    q4 =  models.BooleanField(default=False)
    q5 = models.TextField(null=True, blank= True, default='')
    q6 = models.TextField(null=True, blank= True, default='')

    def __str__(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name


    @classmethod
    def get(cls,user):
        try:
            user_ng = cls.objects.get(user=user)
        except cls.DoesNotExist:
            user_ng = cls.objects.create(user=user)
            user_ng.save()
        return user_ng

    def update_nbr_played(self):
        self.nbr_played = len(Experiment.objects.filter(xp_config__xp_cfg_name="normal",user=self.user,is_complete=True))
        self.nbr_won = len(Experiment.objects.filter(xp_config__xp_cfg_name="normal",user=self.user,game_won=True))
        self.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        UserNG.objects.create(user=instance)


class Word(models.Model):
    word = models.CharField(max_length=200,unique=True)
    #experiment = models.ManyToManyField(Experiment,null=True)
    def __str__(self):
        return self.word

class Role(models.Model):
    role = models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.role

class Meaning(models.Model):
    #experiment = models.ManyToManyField(Experiment,null=True)
    #meaning = models.IntegerField()
    meaning = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.meaning

    @classmethod
    def get_mlist(cls,M=None,avoid_if_possible=[]):
        m_l = copy.deepcopy(MEANING_LIST)
        for m_av in avoid_if_possible:
            if (M is None or len(m_l) > M) and m_av in m_l:
                m_l.remove(m_av)
        random.shuffle(m_l)
        return m_l[:M]


class XpConfig(models.Model):
    xp_config = models.CharField(max_length=2000,unique=True)
    xp_cfg_name = models.CharField(max_length=200,null=True,blank=True)
    score_max = models.IntegerField(default=500)
    def __str__(self):
        return self.xp_config

class Experiment(models.Model):
    xp_config = models.ForeignKey(XpConfig, on_delete=models.PROTECT)
    xp_uuid = models.CharField(max_length=200,default='')
    user_agent_uuid = models.CharField(max_length=200,default='')
    interaction_counter = models.IntegerField(default=0)
    max_interaction = models.IntegerField(default=50)
    exit_value = models.FloatField(default=0)
    meanings = models.ManyToManyField(Meaning,related_name='meanings')
    words = models.ManyToManyField(Word,related_name='words')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    last_ms = models.ForeignKey(Meaning, on_delete=models.PROTECT,related_name='last_ms',null=True)#,blank=True)
    last_mh = models.ForeignKey(Meaning, on_delete=models.PROTECT,related_name='last_mh',null=True)#,blank=True)
    last_w = models.ForeignKey(Word, on_delete=models.PROTECT,related_name='last_w',null=True)#,blank=True)
    last_role = models.CharField(max_length=200,default='')
    last_bool_succ = models.BooleanField(default=False)
    last_nb_skipped = models.IntegerField(default=0)
    size = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True,null=True,default=null_date)
    game_won = models.BooleanField(default=False)

    #Has the player seen the informations on the experiment before this game ?
    before_info = models.BooleanField(default=False)
    #Experiment number for the user
    xp_number = models.IntegerField(default=-1)
    #For the Admin interface
    is_complete = models.BooleanField(default = False)

    def __str__(self):
        return str(self.xp_uuid) + ' ' + str(self.xp_config.xp_config)

    def init_xp(self):
        db = ngal.ngdb.NamingGamesDB(db_type='psycopg2',conn_info="host='db' dbname='naminggames' user='naminggames' password='naminggames'")
        self.xp = db.get_experiment(force_new=True,db_type='postgres',conn_info="host='db' dbname='naminggames' user='naminggames' password='naminggames'",**json.loads(self.xp_config.xp_config))
        self.xp_uuid = self.xp.uuid
        self.xp.init_poplist()
        self.xp._poplist.compress()
        #self.xp.continue_exp_until(0)
        #self.xp.commit_to_db()
        self.save()

        self.update_words()
        self.update_meanings()
        self.get_user_agent_uuid()
        self.xp._poplist.compress()
        self.xp.commit_to_db()
        self.save()

    def save(self,*args,**kwargs):
        # self.update_size()
        return models.Model.save(self,*args,**kwargs)

    # def update_size(self):
    #     ag_list = Agent.objects.filter(xp=self)
    #     if ag_list:
    #         self.size = len(ag_list) + 1
    #     else:
    #         xp_obj = self.get_xp()
    #         self.size = xp_obj._poplist.get_last().get_size()

    def get_xp(self):
        if not hasattr(self,'xp'):
            db = ngal.ngdb.NamingGamesDB(db_type='psycopg2',conn_info="host='db' dbname='naminggames' user='naminggames' password='naminggames'")
            self.xp = db.get_experiment(xp_uuid=self.xp_uuid)
        return self.xp

    @classmethod
    def get_new_xp(cls,user,xp_cfg_name="normal"):
        if xp_cfg_name == "basic":
            size = 3
            xp_cfg["pop_cfg"]["nbagent"] = 3
            xp_cfg["pop_cfg"]["env_cfg"]["M"] = 2
            xp_cfg["pop_cfg"]["env_cfg"]["W"] = 6
            max_inter = 10
        elif xp_cfg_name == "normal":
            size = 5
            M = 5
            xp_cfg["pop_cfg"]["nbagent"] = size
            xp_cfg["pop_cfg"]["env_cfg"]["M"] = M
            xp_cfg["pop_cfg"]["env_cfg"]["m_list"] = Meaning.get_mlist(M=M,avoid_if_possible=[0,1])
            xp_cfg["pop_cfg"]["env_cfg"]["W"] = 6
            max_inter = 50
        elif xp_cfg_name == "multiuser":
            size = 1
            M = 5
            xp_cfg["pop_cfg"]["nbagent"] = size
            xp_cfg["pop_cfg"]["env_cfg"]["M"] = M
            xp_cfg["pop_cfg"]["env_cfg"]["m_list"] = Meaning.get_mlist(M=M,avoid_if_possible=[0,1])
            xp_cfg["pop_cfg"]["env_cfg"]["W"] = 6
            max_inter = 50
        xp_cfg_json = json.dumps(xp_cfg)
        xpcfg_list = XpConfig.objects.filter(xp_config=xp_cfg_json)
        if xpcfg_list:
            xp_conf_model = xpcfg_list.first()
        else:
            xp_conf_model = XpConfig(xp_config=xp_cfg_json,xp_cfg_name=xp_cfg_name,score_max=100*xp_cfg["pop_cfg"]["env_cfg"]["M"])
            xp_conf_model.save()
        xp = Experiment(xp_config=xp_conf_model,user=user,max_interaction=max_inter,size=size)
        xp.init_xp()
        # if xp_cfg_name == 'multiuser':
        #     for i in range(4):
        #         ag = Agent.create()
        #         ag.add_to_xp(xp)
        return xp

    def continue_xp(self,steps=1):
        xp = self.get_xp()
        xp.continue_exp(dT=steps)
        #self.interaction_counter += steps
        self.interaction_counter = xp._T[-1]
        self.save()

    def update_results(self):
        xp = self.get_xp()
        gr = xp.graph(method='srtheo')
        if gr._Y[0]:
            self.exit_code = gr._Y[0][-1]
        self.save()

    def get_result_tab(self,normalized_w=False,normalized_ag=True):
        xp = self.get_xp()
        ag_list = xp._poplist.get_last()._agentlist
        nb_ag = len(ag_list)
        w_list = [w.word for w in self.words.all()]
        m_list = [int(m.meaning) for m in self.meanings.all()]
        ans = {}
        for m in m_list:
            ans[m] = {}
            for ag in ag_list:
                kw_l = ag._vocabulary.get_known_words(m=m)
                for w in kw_l:
                    delta = 1
                    if normalized_ag:
                        delta *= 1./nb_ag
                    if normalized_w:
                        delta *= 1./len(kw_l)
                    if w in list(ans[m].keys()):
                        ans[m][w] += delta
                    else:
                        ans[m][w] = delta
        return ans

    def get_currentgame_json(self):
        filename = './data/current_game_info/'+self.xp_uuid+'.txt'
        with open(filename,'r') as f:
            currentgame_json = json.loads(f.read())
        return currentgame_json

    def save_currentgame_json(self,currentgame_json):
        filename = './data/current_game_info/'+self.xp_uuid+'.txt'
        with open(filename,'w') as f:
            f.write(json.dumps(currentgame_json))

    def get_user_agent_uuid(self):
        if self.user_agent_uuid == '':
            xp = self.get_xp()
            ag = xp._poplist.get_last()._agentlist[0]
            #print(ag._id)
            self.user_agent_uuid = ag._id
        self.save()
        return self.user_agent_uuid

    def get_last_bool_succ(self):
        xp = self.get_xp()
        return xp._poplist.get_last()._lastgameinfo[3]

    def get_last_mh(self):
        xp = self.get_xp()
        return xp._poplist.get_last()._lastgameinfo[2]

    def update_words(self):
        xp = self.get_xp()
        ag = xp._poplist.get_last()._agentlist[0]
        #print(ag._id)
        w_list = sorted(ag._vocabulary.get_accessible_words())
        #self.words.clear()
        for w in w_list:
            obj_list = Word.objects.filter(word=w)
            if len(obj_list) == 0:
                w_obj = Word.objects.create(word=w)
            else:
                w_obj = obj_list[0]
            try:
                self.words.add(w_obj)
            except:
                print('Adding already present word ',w)
        self.save()

    def update_meanings(self):
        xp = self.get_xp()
        ag = xp._poplist.get_last()._agentlist[0]
        #print(ag._id)
        m_list = sorted(ag._vocabulary.get_accessible_meanings())

        str1 = str(self.meanings)


        #self.meanings.clear()
        str2 = str(self.meanings)


        for m in m_list:
            obj_list = Meaning.objects.filter(meaning=str(m))
            if len(obj_list) == 0:
                m_obj = Meaning.objects.create(meaning=str(m))
            else:
                m_obj = obj_list[0]

            try :
                self.meanings.add(m_obj)
            except :
                print('Adding already present meaning ',m)


        self.save()

#     def exchange_agent(self, nb_to_give, nb_to_take):
#         player_agents = Agent.objects.filter(xp=self)
#         pool_agents = Agent.objects.filter(xp=None)

#         if len(pool_agents) < nb_to_take:
#             for x in range(nb_to_take - len(pool_agents)):
#                 ag = Agent.create()
#                 ag.add_to_xp(None)
#             pool_agents = Agent.objects.filter(xp=None)

# #        agents_to_give = player_agents.shuffle()[:nb_to_give]
#         agents_to_give = list(player_agents.order_by('?')[:nb_to_give])
# #        agents_to_take = pool_agents.shuffle()[:nb_to_take]
#         agents_to_take = list(pool_agents.order_by('?')[:nb_to_take])

#         for agent in agents_to_give:
#             #self.get_xp().rm_agent(agent.ngagent_id)
#             agent.add_to_xp(None)

#         for agent in agents_to_take:
#             #self.get_xp().add_agent(agent.get_ng_agent())
#             agent.add_to_xp(self)

    def add_word_to_user(self,w):
        xp_obj = self.get_xp()
        pop_obj = xp_obj._poplist.get_last()
        ag_obj = pop_obj._agentlist[0]
        ag_obj.discover_words([w])
        xp_obj.save_pop()

    # def transfer_agents(self):
    #     player_agents = Agent.objects.filter(xp=self)
    #     for agent in player_agents:
    #         agent.add_to_xp(None,rm_from_xpobj=False)

    #Has the experiment been completed ? (For the admin interface)
    def update_complete(self):
        self.is_complete = (self.interaction_counter >= self.max_interaction)
        self.save()

class Agent(models.Model):
    xp = models.ForeignKey(Experiment, on_delete=models.CASCADE, blank=True, null=True)
    ngagent = models.BinaryField()
    ngagent_id = models.CharField(max_length=200,default='')

    def get_ng_agent(self):
        if self.ngagent is None:
            raise TypeError('Agent.ngagent is None, not blob')
        else:
            return pickle.loads(self.ngagent)

    def add_to_xp(self, xp,rm_from_xpobj=True):
        if xp is not None:
            xp.get_xp().add_agent(self.get_ng_agent())
        else:
            xp_old = self.xp
            if xp_old is not None:
                ngag = xp_old.get_xp().get_agent(self.ngagent_id)
                self.ngagent = pickle.dumps(ngag)
                if rm_from_xpobj:
                    xp_old.get_xp().rm_agent(ngag)
                xp_old.save()
        self.xp = xp
        if xp is not None:
            self.xp.save()
        self.save()

    @classmethod
    def create(cls):
        nga = ngal.ngagent.Agent(xp_cfg['pop_cfg']['voc_cfg'], xp_cfg['pop_cfg']['strat_cfg'])
        nga.discover_meanings(range(5))
        nga.discover_words(['balabu'])
        ngagent = pickle.dumps(nga)
        ngagent_id = nga._id
        return cls(ngagent=ngagent,ngagent_id=ngagent_id)

class PastInteraction(models.Model):
    #meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    #word = models.ForeignKey(Word, on_delete=models.CASCADE)
    #bool_succ = models.IntegerField()
    #role = models.ForeignKey(Role, on_delete=models.CASCADE)
    meaning = models.CharField(max_length=20)
    meaning_h = models.CharField(max_length=20)
    word = models.CharField(max_length=20)
    bool_succ = models.IntegerField()
    time_id = models.IntegerField()
    role = models.CharField(max_length=20)
    experiment = models.ForeignKey(Experiment,null=True, on_delete=models.CASCADE)#, default=Experiment.objects.all()[0])
    #xp_uuid = models.CharField(max_length=200,default = '')
    def __str__(self):
        return str(self.meaning) + ' ' +str(self.word) + ' ' +str(self.role) + ' ' + str(self.bool_succ)


class Score(models.Model):
    experiment = models.ForeignKey(Experiment,null=True, on_delete=models.CASCADE)#, default=Experiment.objects.all()[0])
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

# A compléter
class Results(models.Model):
    pass


class CookieId(models.Model):
    value = models.CharField(max_length=50)
    users = models.ManyToManyField(User,related_name='users')
