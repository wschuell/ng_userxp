//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"en": {"header_home": "THE NAMING GAME", "skipped_text": "Others were interacting, without you", "not_involved": "One interaction happened without you being a part of it.", "hearer_header_text": "You are the HEARER!", "best_scores": "Best Scores", "result_success": "This interaction was SUCCESSFUL, the hearer understood what the speaker meant to communicate.", "score_text": "This is the score that you obtained. You can do another experiment and try to do better!", "some_id_of_a_string_div": "I am a string", "logoutbutton": "Logout", "speaker_word_question": "Using which word?", "img_interaction_text": "<b>Example of an interaction:</b> The speaker chooses an object or meaning, then a word he thinks is associated to it. Finally, the hearer interpretes the word as a meaning. If the two meanings are the same, the communication was successful.<br><br> In an interaction, you are sometimes the speaker, sometimes the hearer, and sometimes you are not involved.", "text_button_basic": "Tutorial, easy. It should take 1-2min", "new_experiment": "New experiment", "speaker_meaning_question": "What do you want to talk about?", "homebutton": "Home", "home_you": "This is you!", "speaker_header_text": "You are the SPEAKER!", "window_title": "The Naming Game", "interactbutton": "Interact", "result_fail": "This interaction FAILED, the hearer did not understand what the speaker was referring to but will remember the association.", "header_inter": "Interaction", "text_button_normal": "Normal. It should take 5-7 min", "button_normal": "Normal", "hearer_word_question": "You heard this word :", "title": "English title", "hometext": "Agree on a common vocabulary with a group of individuals by interacting with them.", "button_basic": "Basic", "button_start": "Start", "hearer_meaning_question": "What do you think the speaker was talking about?", "not_involved_pre": "", "button_next": "Next", "text_choice": "Choose a type of experiment:", "not_involved_post": " interactions happened without you being a part of it.", "home_others": "The others!<br>(You are interacting with them)", "past_interactions": "Past Interactions", "score_header": "End of the experiment", "new_xp": "You are about to begin a new experiment.", "hometitle": "Build a language!", "new_xp_button": "New experiment"}, "it": {"header_home": "IL NAMING GAME", "skipped_text": "Non eri coinvolto in questa interazione", "not_involved": "C'\u00e8 stata un'interazione che NON ti ha coinvolto.", "hearer_header_text": "Sei l'HEARER!", "best_scores": "Hall of Fame", "result_success": "Questa interazione \u00e8 RIUSCITA, l'Hearer ha capito cosa intendesse communicare lo Speaker.", "score_text": "Questo \u00e8 il tuo punteggio per questa partita. Prova ancora per migliorarlo!", "some_id_of_a_string_div": "Sono una stringa", "logoutbutton": "Esci", "speaker_word_question": "Utilizzando quale parola?", "img_interaction_text": "<b>Esempio di interazione:</b> Lo Speaker sceglie un oggetto, poi una parola che, secondo lui, pu\u00f2 essere associata all'oggetto. Infine l'Hearer interpreta la parola, scegliendo un oggetto che, secondo lui, pu\u00f2 esservi associata. Se l'oggetto \u00e8 lo stesso scelto dallo Speaker, la comunicazione \u00e8 avvenuta con success.<br><br> In un'interazione, sei a volte lo speaker, a volte l'hearer, o a volte non sei coinvolto nell'interazione.", "text_button_basic": "Tutoriale, semplice. Dovrebbe bisognare 1-2min", "new_experiment": "Nuovo esperimento", "speaker_meaning_question": "Di cosa vuoi parlare?", "homebutton": "Home", "home_you": "Tu!", "speaker_header_text": "Sei lo SPEAKER!", "window_title": "Il Naming Game", "interactbutton": "Interagisci", "result_fail": "Questa interazione NON \u00e8 RIUSCITA, l'Hearer NON ha capito cosa intendesse communicare lo Speaker, pero si ricordara di quell'associazione.", "header_inter": "Interazione", "text_button_normal": "Normale. Dovrebbe bisognare 5-7 min", "button_normal": "Normale", "hearer_word_question": "Hai ascoltato questa parola:", "title": "Titolo italiano", "hometext": "Crea un nuovo vocabolario per comunicare con persone che non parlano la tua stessa lingua appartenenti a una diversa popolazione.", "button_basic": "Basico", "button_start": "Comincia", "hearer_meaning_question": "Di cosa pensi lo Speaker stia parlando?", "not_involved_pre": "Ci sono state ", "button_next": "Continua", "text_choice": "Scegli un tipo di esperimento:", "not_involved_post": " interazioni riuscite che NON ti hanno coinvolto.", "home_others": "Gli altri!<br>(Proverai a comunicare con loro)", "past_interactions": "Interazioni passate", "score_header": "Fine dell'esperimento", "new_xp": "Stai per iniziare un nuovo esperimento.", "hometitle": "Costruisci un linguaggio!", "new_xp_button": "Nuovo esperimento"}};
//LANG GETS DECLARED HERE, this line is used in the python script generating it



    function change_language(lang_str){
        var current_lang = lang[lang_str];
        $('#some_id_of_a_string_div').html(current_lang.some_id_of_a_string_div);
        $('#hearer_header_text').html(current_lang.hearer_header_text);
        $('#speaker_header_text').html(current_lang.speaker_header_text);
        $('#past_interactions').html(current_lang.past_interactions);
        $('#result_success').html(current_lang.result_success);
        $('#result_fail').html(current_lang.result_fail);
        $('#speaker_word_question').html(current_lang.speaker_word_question);
        $('#speaker_meaning_question').html(current_lang.speaker_meaning_question);
        $('#hearer_word_question').html(current_lang.hearer_word_question);
        $('#hearer_meaning_question').html(current_lang.hearer_meaning_question);
        $('#not_involved').html(current_lang.not_involved);
        $('#header_inter').html(current_lang.header_inter);
        $('#new_xp').html(current_lang.new_xp);
        $('#homebutton').html(current_lang.homebutton);
        $('#logoutbutton').html(current_lang.logoutbutton);
        $('#button_next').html(current_lang.button_next);
        $('#button_start').html(current_lang.button_start);
        $('#new_xp_button').html(current_lang.new_xp_button);
        $('#new_experiment').html(current_lang.new_experiment);
        $('#hometext').html(current_lang.hometext);
        $('#header_home').html(current_lang.header_home);
        $('#hometitle').html(current_lang.hometitle);
        $('#score_header').html(current_lang.score_header);
        $('#score_text').html(current_lang.score_text);
        $('#home_others').html(current_lang.home_others);
        $('#home_you').html(current_lang.home_you);
        $('#window_title').html(current_lang.window_title);
        $('#img_interaction_text').html(current_lang.img_interaction_text);
        $('#interactbutton').html(current_lang.interactbutton);
        $('#skipped_text').html(current_lang.skipped_text);
        $('#best_scores').html(current_lang.best_scores);
        $('#text_choice').html(current_lang.text_choice);
        $('#button_normal').html(current_lang.button_normal);
        $('#button_basic').html(current_lang.button_basic);
        $('#text_button_normal').html(current_lang.text_button_normal);
        $('#text_button_basic').html(current_lang.text_button_basic);

        //$(document).prop('title', current_lang.title);
        //$('#title').html(lang.it[0].some_id_of_a_string_div);
        //$('text#button_next').val(lang.it[0].button_next);
        if ($('#not_involved').attr('nb_skipped') && $('#not_involved').attr('nb_skipped') != "1"){
            var replace_string = current_lang.not_involved_pre + $('#not_involved').attr('nb_skipped') + current_lang.not_involved_post;
            $('#not_involved').html(replace_string);
        };


    Cookies.set('NamingGameLang',
        lang_str
        );
        $('html').attr('lang',lang_str);
        if (lang_str == "en"){$("#flag_it").show();$("#flag_en").hide();};
        if (lang_str == "it"){$("#flag_en").show();$("#flag_it").hide();};
    };


function set_language(){
    if (typeof Cookies.get('NamingGameLang') === 'undefined'){
        var html_lang = $('html').attr('lang');
    } else {
        var html_lang = Cookies.get('NamingGameLang');
        $('html').attr('lang',html_lang);
    };
    change_language(html_lang);
    //$('#flag_'+html_lang).trigger("click");
};






$( document ).ready(function(){


        $.each(lang,function(key,value){

    $('#flag_'+key).click(function(event){
        change_language(key);
    });
});



    set_language();
}
    );
