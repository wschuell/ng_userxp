//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"en": {"result_success": "This interaction was SUCCESSFUL", "result_fail": "This interaction FAILED", "not_involved": "You were not involved in this interaction.", "new_experiment": "New experiment", "homebutton": "Home", "speaker_header_text": "You are the SPEAKER!", "hearer_word_question": "You heard this word :", "title": "English title", "button_start": "Start", "logoutbutton": "Logout", "button_next": "Next", "hearer_header_text": "You are the HEARER!", "some_id_of_a_string_div": "I am a string", "speaker_word_question": "Using which word?", "speaker_meaning_question": "What do you want to talk about?", "not_involved_pre": "You were not involved in ", "header_inter": "Interaction", "best_scores": "Best Scores", "hometext": "Hometext", "hearer_meaning_question": "What do you think the speaker talked about?", "not_involved_post": " interactions", "past_interactions": "Past Interactions", "new_xp": "This experiment has not started yet.", "hometitle": "HOMETITLE", "new_xp_button": "New experiment"}, "it": {"result_success": "Questa interazione era un SUCCESSO", "result_fail": "Questa interazione era una FAILURE", "not_involved": "Non eri parte de quella interazione", "new_experiment": "Nuovo esperimento", "homebutton": "Home", "speaker_header_text": "Sei il SPEAKER!", "hearer_word_question": "Hai sentito questa parola :", "title": "Titolo italiano", "button_start": "Comincia", "logoutbutton": "Sconnettarsi", "button_next": "Continua", "hearer_header_text": "Sei il HEARER!", "some_id_of_a_string_div": "Sono una stringa", "speaker_word_question": "Utilizzando che parola?", "speaker_meaning_question": "De cosa vuoi parlare?", "not_involved_pre": "Non eri parte de ", "header_inter": "Interazione", "best_scores": "Migliori Giochi", "hometext": "Hometext", "hearer_meaning_question": "De cosa pensi il speaker ha parlato?", "not_involved_post": " interazioni", "past_interactions": "Interazioni pasate", "new_xp": "Quell esperimento ancora non e cominciato.", "hometitle": "HOMETITLE", "new_xp_button": "Nuovo esperimento"}};
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
        $('#hometitle').html(current_lang.hometitle);
        $(document).prop('title', current_lang.title);
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
