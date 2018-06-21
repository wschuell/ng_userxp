
# coding: utf-8
import json

dict_obj = {
	"it" : {
		"some_id_of_a_string_div": "Sono una stringa" ,
		"title": "Titolo italiano",
		"button_next": "Continua",
        "hearer_header_text": "Sei l'HEARER!",
        "speaker_header_text": "Sei lo SPEAKER!",
        "past_interactions": "Interazioni passate",
        "result_success": "Questa interazione è RIUSCITA, l'Hearer ha capito cosa intendesse communicare lo Speaker.",
        "result_fail": "Questa interazione NON è RIUSCITA, l'Hearer NON ha capito cosa intendesse communicare lo Speaker, pero si ricordara di quell'associazione.",
        "hearer_word_question":"Hai ascoltato questa parola:",
        "hearer_meaning_question":"Di cosa pensi lo Speaker stia parlando?",
        "speaker_word_question":"Utilizzando quale parola?",
        "speaker_meaning_question":"Di cosa vuoi parlare?",
        "new_xp": "Stai per iniziare un nuovo esperimento.",
        "not_involved": "C'è stata un'interazione che NON ti ha coinvolto.",
        "not_involved_pre": "Ci sono state ",
        "not_involved_post": " interazioni riuscite che NON ti hanno coinvolto.",
        "header_inter":"Interazione",
        "homebutton":"Home",
        "new_xp_button":"Nuovo esperimento",
        "new_experiment":"Nuovo esperimento",
        "logoutbutton":"Esci",
        "best_scores":"Hall of Fame",
        "hometitle":"Costruisci un linguaggio!",
        "hometext":"Crea un nuovo vocabolario per comunicare con persone che non parlano la tua stessa lingua appartenenti a una diversa popolazione.",
        "button_start":"Comincia",
        "score_header":"Fine dell'esperimento",
        "score_text":"Questo è il tuo punteggio per questa partita. Prova ancora per migliorarlo!",
        "window_title":'Il Naming Game',
        "header_home":"IL NAMING GAME",
        "home_others":'Gli altri!<br>(Proverai a comunicare con loro)',
        "home_you":'Tu!',
        "img_interaction_text":"<b>Esempio di interazione:</b> Lo Speaker sceglie un oggetto, poi una parola che, secondo lui, può essere associata all'oggetto. Infine l'Hearer interpreta la parola, scegliendo un oggetto che, secondo lui, può esservi associata. Se l'oggetto è lo stesso scelto dallo Speaker, la comunicazione è avvenuta con success.<br><br> In un'interazione, sei a volte lo speaker, a volte l'hearer, o a volte non sei coinvolto nell'interazione.",
        "skipped_text":"Non eri coinvolto in questa interazione",
        "interactbutton":"Interagisci",
        "text_choice":"Scegli un tipo di esperimento:",
        "button_basic":"Basico",
        "button_normal":"Normale",
        "text_button_basic":"Tutoriale, semplice. Dovrebbe bisognare 1-2min",
        "text_button_normal":"Normale. Dovrebbe bisognare 5-7 min",
    },
    "en" : {
        "some_id_of_a_string_div": "I am a string" ,
        "title": "English title",
        "button_next": "Next",
        "hearer_header_text": "You are the HEARER!",
        "speaker_header_text": "You are the SPEAKER!",
        "past_interactions": "Past Interactions",
        "result_success": "This interaction was SUCCESSFUL, the hearer understood what the speaker meant to communicate.",
        "result_fail": "This interaction FAILED, the hearer did not understand what the speaker was referring to but will remember the association.",
        "hearer_word_question":"You heard this word :",
        "hearer_meaning_question":"What do you think the speaker was talking about?",
        "speaker_word_question":"Using which word?",
        "speaker_meaning_question":"What do you want to talk about?",
        "new_xp": "You are about to create a new language.",
        "not_involved": "One interaction happened without you being a part of it.",
        "not_involved_pre": "",
        "not_involved_post": " interactions happened without you being a part of it.",
        "header_inter":"Interaction",
        "homebutton":"Home",
        "new_xp_button":"New experiment",
        "new_experiment":"New experiment",
        "logoutbutton":"Logout",
        "best_scores":"Best Scores",
        "button_start":"Start",
        "hometitle":"Build a language!",
        "header_home":"THE NAMING GAME",
        "hometext":"Agree on a common vocabulary with a group of individuals by interacting with them.",
        "score_header":"End of the experiment",
        "score_text":"This is the score that you obtained. You can do another experiment and try to do better!",
        "window_title":'The Naming Game',
        "home_others":'The others!<br>(You are interacting with them)',
        "home_you":'This is you!',
        "img_interaction_text":"A language is not extraordinarly useful if you have nobody to talk with, so you need to agree with other people on what each word means. This is done through a series of interactions with other people.<br><br>In each interaction, there are two people. One—the <b>speaker</b>—says a word. The other—the <b>hearer</b>—shows what the word means to him. If the meaning of the word for the hearer is the same as the speaker, the interaction is successful, and the association between the word and the meaning is reinforced in both the speaker and the hearer.<br><br>You will sometimes be the hearer, sometimes the speaker, and many interactions will happen between other people, without you.",
        "skipped_text":"Others were interacting, without you",
        "interactbutton":"Interact",
        "text_choice":"Choose a type of experiment:",
        "button_basic":"Basic",
        "button_normal":"Normal",
        "text_button_basic":"Tutorial, easy. It should take 1-2min",
        "text_button_normal":"Normal. It should take 5-7 min",
    }
}




json_str = "\nvar lang = "+json.dumps(dict_obj)+";\n"

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
