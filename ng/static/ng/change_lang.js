

    $('#flag_it').click(function(event){
        var current_lang = lang.it;
        // there's a cleaner, one line solution, but maybe it is not worth wasting time in this case since text isn't a lot
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
        $(document).prop('title', current_lang.title);
        //$('#title').html(lang.it[0].some_id_of_a_string_div);
        $('#new_xp_button').attr('value',current_lang.new_xp_button);
        $('#button_next').attr('value',current_lang.button_next);
        //$('text#button_next').val(lang.it[0].button_next);

    Cookies.set('NamingGameLang',
        'it'
        );
        $('html').attr('lang','it');
    });

    $('#flag_en').click(function(event){
        var current_lang = lang.en;
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
        $(document).prop('title', current_lang.title);
        //$('#some_other_id_of_a_string_div').html(lang.it[0].some_id_of_a_string_div)
        $('#new_xp_button').attr('value',current_lang.new_xp_button);
        $('#button_next').attr('value',current_lang.button_next);
        //$('text#button_next').val(lang.en[0].button_next);

    Cookies.set('NamingGameLang',
        'en'
        );
        $('html').attr('lang','en');
    });

    if (typeof Cookies.get('NamingGameLang') === 'undefined'){
        var html_lang = $('html').attr('lang');
    } else {
        var html_lang = Cookies.get('NamingGameLang');
        $('html').attr('lang',html_lang);
    };

    $('#flag_'+html_lang).trigger("click");