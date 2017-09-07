//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"en": {"header_home": "THE NAMING GAME", "skipped_text": "Others are interacting, without you", "not_involved": "One interaction happened without you being a part of it.", "hearer_header_text": "You are the HEARER!", "best_scores": "Best Scores", "result_success": "This interaction was SUCCESSFUL, the hearer understood what the speaker wanted to communicate", "score_text": "This is the score that you obtained. You can do another experiment and try to do better!", "some_id_of_a_string_div": "I am a string", "logoutbutton": "Logout", "speaker_word_question": "Using which word?", "img_interaction_text": "<b>Example of an interaction:</b> The speaker chooses an object or meaning, then a word he thinks is associated to it, and finally the hearer interpretes the word as a meaning. If the two meanings are the same, the communication was successful.", "new_experiment": "New experiment", "speaker_meaning_question": "What do you want to talk about?", "homebutton": "Home", "home_you": "This is you!", "speaker_header_text": "You are the SPEAKER!", "window_title": "The Naming Game", "interactbutton": "Interact", "result_fail": "This interaction FAILED, the hearer did not understand what the speaker was referring to.", "header_inter": "Interaction", "hearer_word_question": "You heard this word :", "title": "English title", "hometext": "Agree on a common vocabulary with a group of individuals by interacting with them.", "button_start": "Start", "hearer_meaning_question": "What do you think the speaker talked about?", "not_involved_pre": "", "button_next": "Next", "not_involved_post": " interactions happened without you being a part of it.", "home_others": "The others, you are interacting with them", "past_interactions": "Past Interactions", "score_header": "End of the experiment", "new_xp": "You are about to begin a new experiment.", "hometitle": "Build a language!", "new_xp_button": "New experiment"}, "it": {"header_home": "IL NAMING GAME", "skipped_text": "Non eri parte de questa interazione", "not_involved": "C era un interazione senza te", "hearer_header_text": "Sei il HEARER!", "best_scores": "Migliori Giochi", "result_success": "Questa interazione era un SUCCESSO, il hearer ha capito cosa intendava communicare il speaker.", "score_text": "Quello e la valore dello tuo score. Puoi rifare un esperimento per provare a fare meglio!", "some_id_of_a_string_div": "Sono una stringa", "logoutbutton": "Sconnettarsi", "speaker_word_question": "Utilizzando che parola?", "img_interaction_text": "<b>Esempio di interazione:</b> Il speaker sceglie un oggetto, poi una parola che per lui ci e associata, e il hearer interpreta la parola come un oggetto. Se i due sono i stessi, la communicazione e un successo.", "new_experiment": "Nuovo esperimento", "speaker_meaning_question": "De cosa vuoi parlare?", "homebutton": "Home", "home_you": "Sei tu!", "speaker_header_text": "Sei il SPEAKER!", "window_title": "Il Naming Game", "interactbutton": "Interagisci", "result_fail": "Questa interazione non era un successo, il hearer non ha capito cosa voleva communicare il speaker.", "header_inter": "Interazione", "hearer_word_question": "Hai sentito questa parola :", "title": "Titolo italiano", "hometext": "Mettite d'accordo su un vocabulario facendo interazioni con individuali da una certa populazione.", "button_start": "Comincia", "hearer_meaning_question": "De cosa pensi il speaker ha parlato?", "not_involved_pre": "C eranno ", "button_next": "Continua", "not_involved_post": " interazioni che hanno successo senza te", "home_others": "Gli altri con chi interagisci", "past_interactions": "Interazioni pasate", "score_header": "Fine dell esperimento", "new_xp": "Stai per cominciare un nuovo esperimento.", "hometitle": "Costruisci un linguagio!", "new_xp_button": "Nuovo esperimento"}};
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
