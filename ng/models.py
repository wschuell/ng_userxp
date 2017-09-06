# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import naminggamesal as ngal

# Create your models here.

import json


class Word(models.Model):
    word = models.CharField(max_length=200)
    #experiment = models.ManyToManyField(Experiment,null=True)
    def __str__(self):
        return self.word

class Role(models.Model):
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.role

class Meaning(models.Model):
    #experiment = models.ManyToManyField(Experiment,null=True)
    #meaning = models.IntegerField()
    meaning = models.CharField(max_length=100)
    def __str__(self):
        return self.meaning

class XpConfig(models.Model):
    xp_config = models.CharField(max_length=2000)
    usage = models.IntegerField(default=0)
    def __str__(self):
        return self.xp_config


class Experiment(models.Model):
    xp_config = models.ForeignKey(XpConfig, on_delete=models.PROTECT)
    xp_uuid = models.CharField(max_length=200,default='')
    user_agent_uuid = models.CharField(max_length=200,default='')
    interaction_counter = models.IntegerField(default=0)
    max_interaction = models.IntegerField(default=100)
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

    def __str__(self):
        return str(self.xp_uuid) + ' ' + str(self.xp_config.xp_config)

    def get_xp(self):
        if not hasattr(self,'xp'):
            db = ngal.ngdb.NamingGamesDB(db_type='psycopg2')
            if self.xp_uuid == '':
                self.xp = db.get_experiment(force_new=True,**json.loads(self.xp_config.xp_config))
                self.xp_uuid = self.xp.uuid
                self.save()
            else:
                self.xp = db.get_experiment(xp_uuid=self.xp_uuid)
        return self.xp

    @classmethod
    def get_new_xp(cls,user):
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
        xp = Experiment(xp_config=xp_conf_obj,user=user)
        xp.get_xp()
        xp.save()
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
            self.user_agent_uuid = xp._poplist.get_last()._agentlist[0]._id
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
        w_list = sorted(ag._vocabulary.get_accessible_words())
        self.words.clear()
        for w in w_list:
            obj_list = Word.objects.filter(word=w)
            if len(obj_list) == 0:
                w_obj = Word.objects.create(word=w)
            else:
                w_obj = obj_list[0]
            self.words.add(w_obj)
        self.save()

    def update_meanings(self):
        xp = self.get_xp()
        ag = xp._poplist.get_last()._agentlist[0]
        m_list = sorted(ag._vocabulary.get_accessible_meanings())
        self.meanings.clear()
        for m in m_list:
            obj_list = Meaning.objects.filter(meaning=str(m))
            #print str(obj_list)
            if len(obj_list) == 0:
                m_obj = Meaning.objects.create(meaning=str(m))
            else:
                m_obj = obj_list[0]

            self.meanings.add(m_obj)
        self.save()

class PastInteraction(models.Model):
    #meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    #word = models.ForeignKey(Word, on_delete=models.CASCADE)
    #bool_succ = models.IntegerField()
    #role = models.ForeignKey(Role, on_delete=models.CASCADE)
    meaning = models.IntegerField()
    meaning_h = models.IntegerField()
    word = models.CharField(max_length=20)
    bool_succ = models.IntegerField()
    time_id = models.IntegerField()
    role = models.CharField(max_length=20)
    experiment = models.ForeignKey(Experiment,null=True)#, on_delete=models.CASCADE, default=Experiment.objects.all()[0])
    #xp_uuid = models.CharField(max_length=200,default = '')
    def __str__(self):
        return str(self.meaning) + ' ' +str(self.word) + ' ' +str(self.role) + ' ' + str(self.bool_succ)


class Score(models.Model):
    experiment = models.ForeignKey(Experiment,null=True)#, on_delete=models.CASCADE, default=Experiment.objects.all()[0])
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class CookieId(models.Model):
    value = models.CharField(max_length=50)
    users = models.ManyToManyField(User,related_name='users')