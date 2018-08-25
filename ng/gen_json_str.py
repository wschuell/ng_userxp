
# coding: utf-8
import json
import sys

dict_obj = {
  'fr':{
    #Global

    #Login
    'welcome': 'Naming Game',
    'enter_player_name': 'Entrez votre nom ici :',
    'label_lang': '',#'Choisissez votre langue:',
    'label_code': 'Si on vous a indiqué un code spécifique, entrez le ici :',
        'consent_form':'''<p>Vous allez jouer à un court jeu lors duquel vous aurez à construire collectivement un lexique avec d'autres individus. Vos réponses seront enregistrées mais resteront anonymes. Ce jeu durera environ 20 minutes.
</p><p style = "margin-top:1.5em;margin-bottom:1.5em;"><b>Avant d'accepter de participer à l'expérience, veuillez <a href="/static/ng/pdf/consent_form_fr.pdf" target="_blank">cliquez ici</a> pour lire les informations détaillées concernant l'expérience.</b>
<ul>
                    <li>Vous avez lu et compris les informations détaillées sur cette recherche.</li>
                    <li>Vous acceptez que vos données annonymisées pourraient être gardées jusqu'à 5 ans dans les archives d'Inria et pourraient être utilisées par des chercheurs qualifiés dans des buts d'enseignement ou de recherche.</li>
                    <li>Vous acceptez que vos données annonymisées pourraient devenir publiquement accessibles pour des usages divers, e.g., diffusées sur internet.</li>
                    <li>Vous consentez à l'usage de cookies sur ce site.</li>
                </ul>
<p>Si vous ne consentez pas à tout cela, fermez simplement la fenêtre dans votre navigateur.</p>
''',
    'submit':'Valider',

    #Home
    'subtitle': 'Créez un nouveau langage.',
    'button_basic': 'TUTORIEL',
    'button_multi': 'BONUS',
    'button_normal': 'JEU',
    'game_locked' : 'Gagner le Tutoriel',
    'multi_locked' : 'Gagner le Jeu 3 fois',

    #Story End
    'story_pagetitle': 'HISTOIRE',
    'results': "RESULTATS",
    'c1_1': ' Vous avez été enlevé par des Extraterrestres !',
    'c1_2': 'Vous <img class="txt_img" src="/static/ng/img/chat.png"> voilà enfermé seul dans une pièce de leur vaisseau. Dans les pièces d\'à côté se trouvent <span class="important">3 autres individus</span> <img src="/static/ng/img/user_groop.png" class="txt_img" style="vertical-align:middle;"> que vos ravisseurs ont également enlevés aux quatre coins de la galaxie.',
    'c2_1':"Pour ce faire, vous ne pourrez parler que <span class='important'>deux par deux</span> grâce à une <span class='important'>radio</span>, <span class='important'>sans savoir lequel de vos camarades d'infortune est à l'autre bout</span>.",
    'c2_2':'L\'un de vous proposera un mot <img src="/static/ng/img/mic-512.png" class="txt_img" > et l\'autre devra deviner l\'objet auquel il fait référence. <img class="txt_img" src="/static/ng/img/bitmap-1.png">',
    'c2_3':'Parfois vous proposerez un mot, parfois vous devinerez l\'objet et parfois encore vous écouterez patiemment votre radio <img src="/static/ng/img/time.png" class="txt_img" > dans l\'attente d\'un signal, pendant que d\'autres joueurs communiquent.',
    'text_end':"Après avoir réussi à vous comprendre, vous mettez au point un plan d'évasion spectaculaire. Vos ravisseurs ne voient rien venir avant qu'il ne soit trop tard. Vous leur volez un vaisseau qu'un de vos camarades pilote pour vous ramener tous paisiblement chez vous.",
    'text_end_lost':'Malheureusement, vos gardiens se rendent compte de votre intention d\'arriver à communiquer avant que vous ne réussissiez à vous comprendre. Ils vous séparent aux 4 coins du vaisseau-prison, et vous vous retrouvez avec de nouveaux voisins de cellule.',
    'text_end_tuto':'Votre gardien est agacé des sons bizarres qui proviennent de votre cellule, et décide vous envoyez dans une autre partie du vaisseau, où par chance il y a plus d\'objets et de voisins de cellule.',
    'text_score':'Vous avez atteint un niveau de compréhension de : ',
    'c1_3':'<span class="important">Aucun de vous ne parle la même langue</span> mais vous voulez tous vous échapper pour pouvoir rentrer chez vous.',
    'c2_4':"Mais attention, vous n'avez à vous tous qu'un <span class='important'>nombre limité de conversations</span> pour réussir !",
    'c2_5':'À tout moment, vous pouvez consulter ce que vous avez appris des autres joueurs en cliquant sur l\'horloge <img src="/static/ng/img/history.png" class="txt_img" >.',

    'col_1':'Objets',
    'col_2':'Mots Préférés',
    'col_3':'Seconds mots préférés',

    #Game
    'you' : "/static/ng/img/chat-min.png",
    'button_next': 'CONTINUER',
    'continue': 'CONTINUER',
    'conversations': 'CONVERSATION',
    'anhearer_text':"On essaye de communiquer avec vous.<br>De quoi vous parle-t-on ?",
    'anspeaker_text':"C’est à vous de prendre la parole.<br> Choissisez l’objet dont vous allez parler.",
    'anabs_text':'conversations ont eu lieu en votre absence',
    'choice_words': 'C’est à vous de prendre la parole.<br> Choissisez le mot que vous allez utiliser pour parler de cet objet.',
    'history_objects':'Objets',
    'history_words':'Mots',
    'history_success':'',
    'modal_title': 'Êtes vous sûr.e ?',
    'modal_body': 'Si vous quittez la partie en cours, celle-ci ne sera pas sauvegardée.',
    'btn_yes': '<p>Quitter la partie</p>',
    'btn_no': '<p>Continuer la partie</p>',

    #Feedback
    'speaker_success': "Bravo, votre interlocuteur vous a compris !",
    'speaker_learn': "Votre coéquipier ne connaissait pas ce mot mais il s'en souviendra pour la prochaine fois !",
    'speaker_failure': "Oups, votre interlocuteur pensait que vous parliez d'autre chose. Il s'en souviendra pour la prochaine fois !",
    'hearer_success': "Bravo, vous avez compris votre interlocuteur ! Vous vous en souviendrez pour la prochaine fois !",
    'hearer_learn': "Voilà ce que votre coéquipier voulait dire, vous vous en souviendrez pour la prochaine fois !",
    'hearer_failure': "Oups, votre interlocuteur voulait parler d'autre chose. Vous vous en souviendrez pour la prochaine fois !",
    'tuto_hearer': "Cliquez sur l'horloge <img src='/static/ng/img/history.png' class='txt_img'> en haut à gauche pour consulter ce que vous avez appris de vos interlocuteurs lors des conversations précédentes.",

    #Error Page
    'error_text': "<span id='error_span'>Oups !</span> Il semblerait qu'une erreur se soit produite ! Vous pouvez tenter de continuer ou revenir à l'accueil pour commencer une nouvelle partie.",
    'btn_home': "Revenir à l'Accueil",
    'btn_continue': 'Continuer',

    #Info page
    'titre_info' : "",
    'info_text': "",
    'label_q1':"Aviez-vous déjà entendu parler des jeux de language ? ",
    'label_q2':"Aviez-vous déjà joué à un jeu de ce type ou participé à une expérience similaire auparavant ?",
    'label_q3':"Avez-vous bien compris ce qui se passait au cours du jeu ? ",
    'label_q4':"Avez-vous eu l'impression d'utiliser une certaine stratégie (ou plusieurs) lors de vos parties ?",
    'label_q5':"Si oui, pourriez-vous la ou les décrire brièvement ?",

    #Tooltips
    'tooltip_example':"Si vous n'avez pas de code, laissez ce champ vide.",
    'results_1' : "Objets",
    'results_2' : "Mots les plus utilisés",
    'hearer_w' : "Vous entendez ce mot :",
    'menu_h': "Afficher l'historique",
    'word_inter': "Le mot utilisé dans cette conversation",
    'last_m_you' : "Ce à quoi vous pensiez",
    'last_m_other' : "Ce à quoi votre coéquipier pensait",
    'dont_know' : "Je ne sais pas",
    'your_role_s' : "Vous parliez",
    'your_role_h': "Vous écoutiez",
    'other_role_s' : "Votre interlocuteur parlait",
    'other_role_h' : "Votre interlocuteur vous écoutait",
    'best_score' : "Meilleurs Scores",
    'you' : "C'est vous !",
    'lang' : "Langue du jeu",
    'logout' : "Déconnexion",
    'groop_3' : "Vous êtes 3",
    'groop_5' : "Vous êtes 5",


    'infos_txt':'''
    <p class="text_content_four" style="text-align:left;font-size:18px;">
    <p class="text_content_four" style="text-align:left;font-size:18px;">Ce jeu a été réalisé par William Schueller et Sandy Manolios, dans le cadre de recherches autour de l'évolution du langage.</p>
    <p class="text_content_four" style="text-align:left;font-size:18px;">Les graphismes et le design ont été réalisés par Atlal Boudir.</p>
    <p class="text_content_four" style="text-align:left;font-size:18px;">Si vous voulez en savoir plus, vous pouvez trouver dans les liens ci-dessous différentes ressources:
<ul style="text-align:left;margin-bottom:4em;">
<li> <a href="http://github.com/wschuell/ng_userxp">Le code opensource</a> servant à générer le site </li>
<li> Une liste de liens vers <a href="http://github.com/wschuell/notebooks_cogsci2018">articles et posters</a> sur le travail théorique associé au jeu </li>
<li> Un lien pour <a href="http://naming-game.space">continuer à jouer</a> en dehors du cadre de l'expérience sur la plateforme Prolific</li>
</ul>
    </p>
            </p>
    ''',

#     '''
#             <p class="text_content_four" style="text-align:center;font-size:18px;">
#            Ce jeu auquel vous venez de jouer est bien plus qu'un jeu.
#             C'est une simulation informatique qui modélise l'apparition et
#             l'évolution du vocabulaire d'une population. On parle aussi de modèle
#             computationnel multi-agent de l'émergence et de l'évolution
#             des conventions lexicales, autrement dit un Naming Game.</p>
#             <p class="text_content_four" style="text-align:center;font-size:18px;">
#               Celui-ci est un peu particulier puisqu'il vous permet de prendre la
#               place d'un de ses agents virtuels et de participer vous aussi à la
#               création de ces conventions lexicales. </p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Vous avez pu remarquer que vos choix ont eu une influence, ou pas, sur ceux des autres agents. Car dans ce jeu tout le mode est à égalité et vous n'êtes pas seul.e à pouvoir influer sur le jeu.</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Le score et le tableau à la fin de chaque partie vous indiquent à quel point vous avez tous réussi à vous mettre d'accord. En 50 interactions seulement, c'est un exercice difficile qui comporte une certaine part de hasard. Mais le succès de chaque partie est loin d'être aléatoire. De très nombreuses stratégies sont possibles et permettent, à votre échelle, d'influencer significativement le résultat.
#               Nous nous penchons ici plus précisément sur la manière dont vous choisissez les objets lorsque c'est à votre tour de parler (on dit aussi que vous êtes le speaker).</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Vous pouvez par exemple choisir complètement au hasard. On appelle cette stratégie une stratégie naïve. Vous pouvez aussi choisir ces objets en fonction de certains critères.
#               Une possibilité serait de parler toujours du même objet. Vous aurez ainsi de grandes chances pour que tout le monde partage le même mot pour cette objet, mais il y a également beaucoup de risques pour que les autres objets se retrouvent sans nom partagé par tous à la fin de la partie.</p>

#             <p  class=" text_content_four" style="text-align:center;font-size:18px;">Une autre stratégie consiste à parler uniquement ou presque des objets dont vous connaissez le nom pour augmenter vos chances que ce nom soit utilisé par le plus grand nombre de vos partenaires.</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Bref, il y a énormément de stratégies et c'est justement ce qui nous intéresse dans le cadre de notre recherche.</p>
# ''',

'infos_title':'MERCI DE VOTRE PARTICIPATION',
'infos_qu':'''
 <p class=" text_content_four" style="text-align:center;font-size:18px;"> Afin de nous aider, pourriez-vous remplir ce bref questionnaire avant de finir l'expérience?</p>
''',
'question_title':'Questionnaire:',

  },

  'en': {
    #Global

    #Login
    'welcome': 'The Naming Game',
    'enter_player_name': 'Enter your name here :',
    'label_lang': '',#'Choose your language :',
    'label_code': 'If you have been told to use a specific token, enter it here :',
    'submit' : "Submit",
        'consent_form':'''<p>You’re about to start a short game where you will have to collectively build a lexicon with other individuals. Your answers will be recorded but will not be identifiable to you personally. The game will take about 20 minutes.
</p>
<p style = "margin-top:1.5em;margin-bottom:1.5em;"><b>Before consenting to participate, please <a href="/static/ng/pdf/consent_form.pdf" target="_blank">click here</a> to read more detailed information about the study.</b>
</p>
<p>
<ul>
                    <li>You have read and understood the detailed information about the study.</li>
                    <li>You agree that your anonymized data may be kept for up to 5 years in the archives of Inria and may be used by qualified researchers for teaching and research purposes</li>
                    <li>You agree that your anonymized data may be made publicly available for general use, e.g., put on the world wide web.</li>
                    <li>You consent to the use of cookies for this site.</li>
                </ul>
</p>
<p>If you do not agree to all of these, simply close this window in your browser now.</p>
''',

    #Home
    'subtitle': 'Build a new language.',
    'button_basic': 'TUTORIAL',
    'button_multi': 'BONUS',
    'button_normal': 'GAME',
    'game_locked' : 'WIN TUTORIAL TO UNLOCK',
    'multi_locked' : 'WIN 3 GAMES TO UNLOCK',

    #Story End
    'story_pagetitle': 'Story',
    'results': 'RESULTS',
    'c1_1': ' You have been kidnapped by Aliens !',
    'c1_2': 'You <img class="txt_img" src="/static/ng/img/chat.png"> are now locked alone in a room of their huge spaceship. In the neighboring rooms, there are <span class="important">3 other individuals</span> <img src="/static/ng/img/user_groop.png" class="txt_img" style="vertical-align:middle;"> also kidnapped by your abductors at the four corners of the galaxy.',
    'c2_1':'To do so, you may only talk <span class="important">by pairs</span> thanks to a <span class="important">radio</span>, <span class="important">without knowing wich one of your fellow prisoners is on the other side</span>.',
    'c2_2':'One of you will say a word  <img src="/static/ng/img/mic-512.png" class="txt_img" > and the other will have to guess which object they are referring to. <img class="txt_img" src="/static/ng/img/bitmap-1.png">',
    'c2_3':'Sometimes you will talk, sometimes you will listen and guess and sometimes you will keep listening to your radio <img src="/static/ng/img/time.png" class="txt_img" > waiting for a signal, while others are conversing. ',
    'text_end':'Once you manage to understand each other, you come up with a cunning plan to escape. Your abductors don’t even see it coming until it’s too late. You steal a ship from them and one of your companions drives you back home with it.',
    'text_end_lost':'Sadly, your abductors realize that you are trying to communicate before you reach an acceptable level of understanding. They split you between different parts of the prison ship, with new cell neighbors.',
    'text_end_tuto':'Your prison guard gets bored by the many strange sounds that are coming from your cell, and decide to send you to another, luckily with more neighbors and more objects.',
    'text_score':'You reached an understanding level of: ',
    'c1_3':'<span class="important">None of you is from the same planet or speaks the same language</span> but you all want the same thing : escape and go back home.',
    'c2_4':'Be careful, you only have a <span class="important">limited number of conversations</span> to succeed !',
    'c2_5':'At any moment, you can have a look at what you learned from the other players by clicking on the clock <img src="/static/ng/img/history.png" class="txt_img" >.',

    'col_1':'Objects',
    'col_2':'Favorite Words',
    'col_3':'Second Favorite Words',

    #Game
    'you' : "/static/ng/img/chat_you.png",
    'button_next': 'CONTINUE',
    'continue': 'CONTINUE',
    'conversations': 'INTERACTION',
    'anhearer_text':"Someone is trying to communicate with you.<br>What are they talking about ?",
    'anspeaker_text':'Your turn to speak. <br> Pick the object you will talk about.',
    'anabs_text':'interactions happened without you being a part of it.',
    'choice_words': 'Your turn to speak. <br> Pick the word you will use to refer to this object.',
    'history_objects':'Objects',
    'history_words':'Words',
    'history_success':'',
    'modal_title': 'Are you sure ?',
    'modal_body': 'If you quit this page, the game won’t be saved. Do you still want to quit ?',
    'btn_yes': '<p>Yes, quit the game</p>',
    'btn_no': '<p>No, resume the game</p>',

    #Feedback
    'speaker_success': "Well done, your partner understood !",
    'speaker_learn': "Your partner didn't know this word but they will remember it next time !",
    'speaker_failure': "Oops, your partner thought you were talking about something else. They will remember it next time !",
    'hearer_success': "Well done, you understood your partner ! You will remember it next time !",
    'hearer_learn': "This is what your partner meant, you will remember it next time !",
    'hearer_failure': "Oops, your partner meant something else. You will remember it next time !",
    'tuto_hearer': "Click on the clock <img src='/static/ng/img/history.png' class='txt_img'> in the upper right corner to see what you learned from the other players in the previous interactions.",


        #Error Page
    'error_text': "<span id='error_span'>Oops!</span> It seems that an error occured. You can try to resume your game or go back to home page.",
    'btn_home': "Home",
    'btn_continue': 'Resume the game',

    #Info page
    'titre_info' : "",
    'info_text': "",
    'label_q1':"Were you already familiar with language games ? ",
    'label_q2':"Have you already played such a game or participated to a similar experiment ?",
    'label_q3':"Did you understand what was happening in the game ?",
    'label_q4':"Did you use a certain strategy (or several) during your games ?",
    'label_q5':"If it is a 'Yes', could you describe it briefly ?",

    #Tooltips
    'tooltip_example':"If you were not provided a token, leave empty.",
    'results_1' : "Objects",
    'results_2' : "Most used words per object",
    'hearer_w' : "You heard this word",
    'menu_h': "Click to see past interactions",
    'word_inter': "The word used in this conversation",
    'last_m_you' : "What you were thinking",
    'last_m_other' :  "What your partner was referring to",
    'dont_know' : "I don't know",
    'your_role_s' : "You spoke",
    'your_role_h': "You listened",
    'other_role_s' : "Your partner spoke",
    'other_role_h' : "Your partner listened",
    'best_score' : "Best Scores",
    'you' : "That's you !",
    'lang' : "Game language",
    'logout' : "Logout",
    'groop_3' : "You are 3",
    'groop_5' : "You are 5",


    'infos_txt':'''
    <p class="text_content_four" style="text-align:left;font-size:18px;">
    <p class="text_content_four" style="text-align:left;font-size:18px;">This game was written by William Schueller and Sandy Manolios, to collect data as a scientific experiment on language evolution.</p>
    <p class="text_content_four" style="text-align:left;font-size:18px;">Graphics and design are the work of Atlal Boudir.</p>
    <p class="text_content_four" style="text-align:left;font-size:18px;">If you want to go further, you can find below a set of links to various resources:
<ul style="text-align:left;margin-bottom:4em;">
<li> <a href="http://github.com/wschuell/ng_userxp">The opensource code</a> used to generate the website </li>
<li> A set of links to <a href="http://github.com/wschuell/notebooks_cogsci2018">articles and explanatory posters and notebooks</a> on the theoretical work behind the game </li>
<li> A link to <a href="http://naming-game.space">continue playing</a> outside of the Prolific experiment.</li>
</ul>
    </p>
            </p>
    ''',
#     'infos_txt':'''
#             <p class="text_content_four" style="text-align:center;font-size:18px;">
#            Ce jeu auquel vous venez de jouer est bien plus qu'un jeu.
#             C'est une simulation informatique qui modélise l'apparition et
#             l'évolution du vocabulaire d'une population. On parle aussi de modèle
#             computationnel multi-agent de l'émergence et de l'évolution
#             des conventions lexicales, autrement dit un Naming Game.</p>
#             <p class="text_content_four" style="text-align:center;font-size:18px;">
#               Celui-ci est un peu particulier puisqu'il vous permet de prendre la
#               place d'un de ses agents virtuels et de participer vous aussi à la
#               création de ces conventions lexicales. </p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Vous avez pu remarquer que vos choix ont eu une influence, ou pas, sur ceux des autres agents. Car dans ce jeu tout le mode est à égalité et vous n'êtes pas seul.e à pouvoir influer sur le jeu.</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Le score et le tableau à la fin de chaque partie vous indiquent à quel point vous avez tous réussi à vous mettre d'accord. En 50 interactions seulement, c'est un exercice difficile qui comporte une certaine part de hasard. Mais le succès de chaque partie est loin d'être aléatoire. De très nombreuses stratégies sont possibles et permettent, à votre échelle, d'influencer significativement le résultat.
#               Nous nous penchons ici plus précisément sur la manière dont vous choisissez les objets lorsque c'est à votre tour de parler (on dit aussi que vous êtes le speaker).</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Vous pouvez par exemple choisir complètement au hasard. On appelle cette stratégie une stratégie naïve. Vous pouvez aussi choisir ces objets en fonction de certains critères.
#               Une possibilité serait de parler toujours du même objet. Vous aurez ainsi de grandes chances pour que tout le monde partage le même mot pour cette objet, mais il y a également beaucoup de risques pour que les autres objets se retrouvent sans nom partagé par tous à la fin de la partie.</p>

#             <p  class=" text_content_four" style="text-align:center;font-size:18px;">Une autre stratégie consiste à parler uniquement ou presque des objets dont vous connaissez le nom pour augmenter vos chances que ce nom soit utilisé par le plus grand nombre de vos partenaires.</p>

#             <p class=" text_content_four" style="text-align:center;font-size:18px;">Bref, il y a énormément de stratégies et c'est justement ce qui nous intéresse dans le cadre de notre recherche. Afin de nous aidez, pourriez-vous remplir ce bref questionnaire ?</p>
# ''',
'infos_title':'THANK YOU FOR PARTICIPATING',
'infos_qu':'''
  <p class=" text_content_four" style="text-align:center;font-size:18px;">Before finishing the experiment, could you fill in this quick survey ?</p>
''',
'question_title':'Quick survey:',

  }
};





json_str = '\nvar lang = '+json.dumps(dict_obj)+';\n'

#print(json_str)
print('Generating lang.js')

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

sys.exit(0)
