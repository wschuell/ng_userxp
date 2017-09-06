import json

dict_obj = {


	"it" :
    		{
    		"some_id_of_a_string_div": "Sono una stringa" ,
    		"title": "Titolo italiano",
    		"button_next": "Continua",
    		"hearer_header_text": "Sei il HEARER!",
    		"speaker_header_text": "Sei il SPEAKER!",
            "past_interactions": "Interazioni pasate",
            "result_success": "Questa interazione era un SUCCESSO, il hearer ha capito cosa intendava communicare il speaker.",
            "result_fail": "Questa interazione non era un successo, il hearer non ha capito cosa voleva communicare il speaker.",
            "hearer_word_question":"Hai sentito questa parola :",
            "hearer_meaning_question":"De cosa pensi il speaker ha parlato?",
            "speaker_word_question":"Utilizzando che parola?",
            "speaker_meaning_question":"De cosa vuoi parlare?",
            "new_xp": "Stai per cominciare un nuovo esperimento.",
            "not_involved": "C era un interazione senza te",
            "not_involved_pre": "C eranno ",
            "not_involved_post": " interazioni che hanno successo senza te",
            "header_inter":"Interazione",
            "homebutton":"Home",
            "new_xp_button":"Nuovo esperimento",
            "new_experiment":"Nuovo esperimento",
            "logoutbutton":"Sconnettarsi",
            "best_scores":"Migliori Giochi",
            "hometitle":"Costruisci un linguagio!",
            "hometext":"Mettite d'accordo su un vocabulario facendo interazioni con individuali da una certa populazione.",
            "button_start":"Comincia",
            "score_header":"Fine dell esperimento",
            "score_text":"Quello e la valore dello tuo score. Puoi rifare un esperimento per provare a fare meglio!",
            "window_title":'Il Naming Game',
            "header_home":"IL NAMING GAME",
            "home_others":'Gli altri con chi interagisci',
            "home_you":'Sei tu!',
            "img_interaction_text":"Esempio di interazione: Il speaker sceglie un oggetto, poi una parola che per lui ci e associata, e il hearer interpreta la parola come un oggetto. Se i due sono i stessi, la communicazione e un successo.",
            }
        ,
    "en" :
            {
            "some_id_of_a_string_div": "I am a string" ,
            "title": "English title",
            "button_next": "Next",
            "hearer_header_text": "You are the HEARER!",
            "speaker_header_text": "You are the SPEAKER!",
            "past_interactions": "Past Interactions",
            "result_success": "This interaction was SUCCESSFUL, the hearer understood what the speaker wanted to communicate",
            "result_fail": "This interaction FAILED, the hearer did not understand what the speaker was referring to.",
            "hearer_word_question":"You heard this word :",
            "hearer_meaning_question":"What do you think the speaker talked about?",
            "speaker_word_question":"Using which word?",
            "speaker_meaning_question":"What do you want to talk about?",
            "new_xp": "You are about to begin a new experiment.",
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
            "home_others":'The others, you are interacting with them',
            "home_you":'This is you!',
            "img_interaction_text":"Example of an interaction: The speaker chooses an object or meaning, then a word he thinks is associated to it, and finally the hearer interpretes the word as a meaning. If the two meanings are the same, the communication was successful.",
    		}

    }


json_str = "\nvar lang = "+json.dumps(dict_obj)+";\n"

print json_str

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

