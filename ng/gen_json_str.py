
# coding: utf-8
import json

dict_obj = {
  'fr':{
    #Global

    #Login
    'welcome': 'Le Naming Game !',
    'enter_player_name': 'Entrez votre nom ici :',
    'label_lang': 'Choisissez la langue du jeu :',
    'label_code': 'Si vous avez un code spécial, entrez le ici :',
    'submit':'Valider',

    #Home
    'subtitle': 'Explorer le langage.',
    'button_basic': 'TUTORIEL',
    'button_multi': 'INFORMATIONS',
    'button_normal': 'JEU',
    'comment_avatar': "<p>C'est vous !</p>",
    'game_locked' : 'Terminer le Tutoriel pour débloquer',
    'multi_locked' : 'Terminer le Jeu 3 fois pour débloquer',

    #Story End
    'story_pagetitle': 'HISTOIRE',
    'end_pagetitle': 'Félicitations',
    'results': "RESULTATS",
    'c1_1': ' Vous avez été enlevé par des Extraterrestres !',
    'c1_2': "Vous voilà enfermé seul dans une pièce de leur vaisseau. Dans les pièces d'à côté se trouvent <span class='important'>4 autres individus</span> que vos ravisseurs ont également enlevés aux quatre coins de la galaxie.",
    'c2_1':"Pour ce faire, vous ne pourrez parler que <span class='important'>deux par deux</span> grâce à une <span class='important'>radio</span>, <span class='important'>sans savoir lequel de vos camarades d'infortune est à l'autre bout</span>.",
    'c2_2':"L'un de vous proposera un mot et l'autre devra deviner l'objet auquel il fait référence.",
    'c2_3':"Parfois vous proposerez un mot, parfois vous devinerez l'objet et parfois encore vous ne ferez pas partie de la conversation et ne saurez pas ce qui s'y est dit.",
    'text_end':"Après avoir réussi à vous comprendre, vous mettez au point un plan d'évasion spectaculaire. Vos ravisseurs ne voient rien venir avant qu'il ne soit trop tard. Vous leur volez un vaisseau qu'un de vos camarades pilote pour vous ramener tous paisiblement chez vous.",
    'text_score':'Score :',
    'c1_3':'<span class="important">Aucun de vous ne parle la même langue</span> mais vous voulez tous vous échapper pour pouvoir rentrer chez vous.',
    'c2_4':"Mais attention, vous n'avez à vous tous qu'un <span class='important'>nombre limité de conversations</span> pour réussir !",

    'col_1':'Objets',
    'col_2':'Mots Préférés',
    'col_3':'Seconds mots préférés',

    #Game
    'button_next': 'CONTINUER',
    'continue': 'CONTINUER',
    'history_name': 'Historique',
    'conversations': 'CONVERSATION',
    'anhearer_text':"on essaye de communiquer avec vous.<br>de quoi vous parle-t-on ?",
    'anspeaker_text':"c’est à vous de prendre la parole.<br> choissisez l’objet dont vous allez parler.",
    'anabs_text':'conversation a eu lieu en votre absence',
    'hearer_expl': 'De quoi vous parle-t-on ?',
    'choice_words': 'c’est à vous de prendre la parole.<br> choissisez le mot que vous allez utiliser pour parler de cet objet.',
    'history_objects':'Objets',
    'history_words':'Mots',
    'history_success':'Succès',
    'modal_title': 'Êtes vous sûr.e ?',
    'modal_body': 'Si vous quittez la partie en cours, celle-ci ne sera pas sauvegardée. Voulez-vous toujours quitter ?',
    'btn_yes': '<p>Oui, quitter la partie</p>',
    'btn_no': '<p>Non, continuer la partie</p>',

    #Error Page
    'error_text': "<span id='error_span'>Oups !</span> Il semblerait qu'une erreur se soit produite ! Vous pouvez tenter de continuer ou revenir à l'accueil pour commencer une nouvelle partie.",
    'btn_home': "Revenir à l'Accueil",
    'btn_continue': 'Continuer',

    #Info page
    'titre_info' : "",
    'info_text': "",
    'label_q1':"Êtiez-vous déjà familier.ère avec le principe des Naming Games ? ",
    'label_q2':"Aviez-vous déjà joué à un jeu de ce type ou participé à une expérience similaire auparavant ?",
    'label_q3':"Êtes-vous familier.ère avec les concepts évoqués plus haut ? ",
    'label_q4':"Avez-vous eu l'impression d'utiliser une certaine stratégie (ou plusieurs) lors de vos parties ?",
    'label_q5':"Si oui, pourriez-vous la ou les décrire brièvement ?",
  },

  'en': {
    #Global

    #Login
    'welcome': 'The Naming Game!',
    'enter_player_name': 'Enter your name here :',
    'label_lang': 'Choose the game language :',
    'label_code': 'If you have a special token, enter it here :',
    'submit' : "Submit",

    #Home
    'subtitle': 'Explore the language.',
    'button_basic': 'TUTORIAL',
    'button_multi': 'INFORMATIONS',
    'button_normal': 'GAME',
    'comment_avatar': "<p>That's you !</p>",
    'game_locked' : 'COMPLETE THE TUTORIAL TO UNLOCK',
    'multi_locked' : 'COMPLETE THE GAME 3 TIMES TO UNLOCK ',

    #Story End
    'story_pagetitle': 'Story',
    'end_pagetitle': 'RESULTS',
    'c1_1': ' You have been kidnapped by Aliens !',
    'c1_2': 'Now, you are locked alone in a room of their huge spaceship. In the rooms next to yours, there are <span class="important">3 other individuals</span> also kidnapped by your abductors at the four corners of the galaxy.',
    'c2_1':'To do so, you may only talk <span class="important">by pairs</span> thanks to a <span class="important">radio</span>, <span class="important">without knowing wich one of your companions in misery is on the other side</span>.',
    'c2_2':'One of you will say a word and the other will have to guess which object he is referring to.',
    'c2_3':'Sometimes you will talk, sometimes you will guess and sometimes you won’t be in the conversation and you won’t know what was said.',
    'text_end':'Once you managed to understand each other, you develop a spectacular escape plan. Your abductors don’t even see it coming until it’s too late. You steal a ship from them and one of your companions drive you back home with it.',
    'text_score':'Score :',
    'c1_3':'<span class="important">None of you is from the same planet or speak the same language</span> but you all want the same thing : escape and go back home.',
    'c2_4':'But careful, you only have a <span class="important">limited number of conversations</span> to succed !',

    'col_1':'Objects',
    'col_2':'Favorite Words',
    'col_3':'Second Favorite Words',

    #Game
    'button_next': 'CONTINUE',
    'continue': 'CONTINUE',
    'history_name': 'Past Interactions',
    'conversations': 'INTERACTION',
    'anhearer_text':"someone is trying to communicate with you.<br>what are they talking about ?",
    'anspeaker_text':'your turn to speak. <br> choose the object you will talk about.',
    'anabs_text':'interactions happened without you being a part of it.',
    'hearer_expl': 'What does it means ?',
    'choice_words': 'your turn to speak. <br> choose the word you will use to talk about this object.',
    'history_objects':'Objects',
    'history_words':'Words',
    'history_success':'Succes',
    'modal_title': 'Are you sure ?',
    'modal_body': 'If you quit the ongoing game, it won’t be saved. Do you still want to quit ?',
    'btn_yes': '<p>Yes, quit the game</p>',
    'btn_no': '<p>No, resume the game</p>',

        #Error Page
    'error_text': "<span id='error_span'>Oops!</span> It seems that an error occured! You can try to resume your game or go back at home page an start a new one.",
    'btn_home': "Go back to Home page",
    'btn_continue': 'Resume the game',

    #Info page
    'titre_info' : "",
    'info_text': "",
    'label_q1':"Were you already familiar with the Naming Games principle ? ",
    'label_q2':"Have you already played such a game or been taking part into a similar experiment ?",
    'label_q3':"Were you already familiar with the concepts evoked above ?",
    'label_q4':"Did you felt like you used a certain strategy (or several) during your games ?",
    'label_q5':"If it is a 'Yes', could you describe it briefly ?",

  },
  'it': {

    #Login
    'welcome': 'Il Naming Game !',
    'enter_player_name': '',
    'label_lang': '',
    'label_code': '',
    'submit' : '',

    #Home
    'subtitle': '',
    'button_basic': '',
    'button_multi': '',
    'button_normal': '',
    'comment_avatar': '<p></p>',
    'game_locked' : 'TEXTE',
    'multi_locked' : 'TEXTE',

    #Story End
    'story_pagetitle': '',
    'end_pagetitle': '',
    'c1_1': ' ',
    'c1_2': '',
    'c2_1':'',
    'c2_2':'',
    'c2_3':'',
    'text_end':' ',
    'text_score':' ',
    'c1_3':'',
    'c2_4':'',

    'col_1':'',
    'col_2':'',
    'col_3':'',

    #Game
    'button_next': '',
    'continue': '',
    'history_name': '',
    'conversations': '',
    'anhearer_text':'',
    'anspeaker_text':'',
    'anabs_text':'',
    'hearer_expl': '',
    'speaker_expl': '',
    'choice_words': '',
    'history_objects':'',
    'history_words':'',
    'history_success':'',
    'modal_title': '',
    'modal_body': '',
    'btn_yes': '',
    'btn_no': '',

    #Error Page
    'error_text': "<span id='error_span'>Oups !</span> ",
    'btn_home': " ",
    'btn_continue': '',

    #Info page
    'titre_info' : "",
    'info_text': "",
    'label_q1':"",
    'label_q2':"",
    'label_q3':"",
    'label_q4':"",
    'label_q5':"",
  }
};





json_str = '\nvar lang = '+json.dumps(dict_obj)+';\n'

print(json_str)

with open('static/ng/lang.js','w') as f:
    f.write(json_str)



with open('static/ng/change_lang.js','r') as f:
    s1 = f.read()

split_str = '//LANG GETS DECLARED HERE, this line is used in the python script generating it'

splitted = s1.split(split_str)
assert len(splitted) >= 3
splitted[1] = json_str
s2 = split_str.join(splitted)


with open('static/ng/change_lang.js','w') as f:
    f.write(s2)
