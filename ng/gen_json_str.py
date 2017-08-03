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
            "result_success": "Questa interazione era un SUCCESSO",
            "result_fail": "Questa interazione era una FAILURE",
            "hearer_word_question":"Hai sentito questa parola :",
            "hearer_meaning_question":"De cosa pensi il speaker ha parlato?",
            "speaker_word_question":"Utilizzando che parola?",
            "speaker_meaning_question":"De cosa vuoi parlare?",
            "new_xp": "Quell esperimento ancora non e cominciato.",
            "not_involved": "Non eri parte de quella interazione",
            "header_inter":"Interazione",
            "homebutton":"Ritornare alla pagina principale",
            "new_xp_button":"Nuovo esperimento",
            "logoutbutton":"Sconnettarsi",
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
            "result_success": "This interaction was SUCCESSFUL",
            "result_fail": "This interaction FAILED",
            "hearer_word_question":"You heard this word :",
            "hearer_meaning_question":"What do you think the speaker talked about?",
            "speaker_word_question":"Using which word?",
            "speaker_meaning_question":"What do you want to talk about?",
            "new_xp": "This experiment has not started yet.",
            "not_involved": "You were not involved in this interaction.",
            "header_inter":"Interaction",
            "homebutton":"Back to main page",
            "new_xp_button":"New experiment",
            "logoutbutton":"Logout",
    		}

    }


json_str = json.dumps(dict_obj)

print json_str

with open('static/ng/lang.js','w') as f:
	f.write("var lang = "+json_str+";")