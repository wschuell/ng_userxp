//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"en": {"header_home": "THE NAMING GAME", "not_involved": "You were not involved in this interaction.", "hearer_header_text": "You are the HEARER!", "best_scores": "Best Scores", "result_success": "This interaction was SUCCESSFUL", "score_text": "This is the score that you obtained. Try to do better!", "some_id_of_a_string_div": "I am a string", "logoutbutton": "Logout", "speaker_word_question": "Using which word?", "img_interaction_text": "Example of an interaction", "new_experiment": "New experiment", "speaker_meaning_question": "What do you want to talk about?", "homebutton": "Home", "home_you": "You", "speaker_header_text": "You are the SPEAKER!", "window_title": "The Naming Game", "result_fail": "This interaction FAILED", "header_inter": "Interaction", "hearer_word_question": "You heard this word :", "title": "English title", "hometext": "Set up a vocabulary by interacting with individuals from a given population.", "button_start": "Start", "hearer_meaning_question": "What do you think the speaker talked about?", "not_involved_pre": "You were not involved in ", "button_next": "Next", "not_involved_post": " interactions", "home_others": "The others", "past_interactions": "Past Interactions", "score_header": "End of the experiment", "new_xp": "This experiment has not started yet.", "hometitle": "Build a language!", "new_xp_button": "New experiment"}, "it": {"header_home": "IL NAMING GAME", "not_involved": "Non eri parte de quella interazione", "hearer_header_text": "Sei il HEARER!", "best_scores": "Migliori Giochi", "result_success": "Questa interazione era un SUCCESSO", "score_text": "Quello e la valore dello tuo score. Prova a fare meglio!", "some_id_of_a_string_div": "Sono una stringa", "logoutbutton": "Sconnettarsi", "speaker_word_question": "Utilizzando che parola?", "img_interaction_text": "Esempio di interazione", "new_experiment": "Nuovo esperimento", "speaker_meaning_question": "De cosa vuoi parlare?", "homebutton": "Home", "home_you": "Tu", "speaker_header_text": "Sei il SPEAKER!", "window_title": "Il Naming Game", "result_fail": "Questa interazione era una FAILURE", "header_inter": "Interazione", "hearer_word_question": "Hai sentito questa parola :", "title": "Titolo italiano", "hometext": "Mettite d'accordo su un vocabulario facendo interazioni con individuali da una certa populazione.", "button_start": "Comincia", "hearer_meaning_question": "De cosa pensi il speaker ha parlato?", "not_involved_pre": "Non eri parte de ", "button_next": "Continua", "not_involved_post": " interazioni", "home_others": "Gli altri", "past_interactions": "Interazioni pasate", "score_header": "Fine dell esperimento", "new_xp": "Quell esperimento ancora non e cominciato.", "hometitle": "Costruisci un linguagio!", "new_xp_button": "Nuovo esperimento"}};
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
