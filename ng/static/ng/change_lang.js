//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"en": {"header_inter": "Interaction", "hearer_word_question": "You heard this word :", "hearer_header_text": "You are the HEARER!", "logoutbutton": "Logout", "title": "English title", "not_involved": "You were not involved in this interaction.", "result_success": "This interaction was SUCCESSFUL", "some_id_of_a_string_div": "I am a string", "homebutton": "Home", "not_involved_pre": "You were not involved in ", "button_next": "Next", "speaker_word_question": "Using which word?", "not_involved_post": " interactions", "new_xp_button": "New experiment", "new_xp": "This experiment has not started yet.", "past_interactions": "Past Interactions", "speaker_meaning_question": "What do you want to talk about?", "hearer_meaning_question": "What do you think the speaker talked about?", "speaker_header_text": "You are the SPEAKER!", "result_fail": "This interaction FAILED"}, "it": {"header_inter": "Interazione", "hearer_word_question": "Hai sentito questa parola :", "hearer_header_text": "Sei il HEARER!", "logoutbutton": "Sconnettarsi", "title": "Titolo italiano", "not_involved": "Non eri parte de quella interazione", "result_success": "Questa interazione era un SUCCESSO", "some_id_of_a_string_div": "Sono una stringa", "homebutton": "Home", "not_involved_pre": "Non eri parte de ", "button_next": "Continua", "speaker_word_question": "Utilizzando che parola?", "not_involved_post": " interazioni", "new_xp_button": "Nuovo esperimento", "new_xp": "Quell esperimento ancora non e cominciato.", "past_interactions": "Interazioni pasate", "speaker_meaning_question": "De cosa vuoi parlare?", "hearer_meaning_question": "De cosa pensi il speaker ha parlato?", "speaker_header_text": "Sei il SPEAKER!", "result_fail": "Questa interazione era una FAILURE"}};
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
        $(document).prop('title', current_lang.title);
        //$('#title').html(lang.it[0].some_id_of_a_string_div);
        $('#new_xp_button').attr('value',current_lang.new_xp_button);
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
