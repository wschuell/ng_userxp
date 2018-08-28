
var current_lang_id = 'en';
var current_lang = langdict[current_lang_id];

    function change_language(lang_str){
        current_lang_id = lang_str;
        current_lang = langdict[lang_str];

        $('#welcome').html(current_lang.welcome);
        $('#enter_player_name').html(current_lang.enter_player_name);
        $('#label_lang').html(current_lang.label_lang);
        $('#label_code').html(current_lang.label_code);
        $('#consent_form').html(current_lang.consent_form);
        $('#submit').val(current_lang.submit);

          //Home
        $('#button_basic').html(current_lang.button_basic);
        $('#button_multi').html(current_lang.button_multi);
        $('#button_normal').html(current_lang.button_normal);
        $('#comment_avatar').html(current_lang.comment_avatar);
        $('#subtitle').html(current_lang.subtitle);
        $('#game_locked' ).html(current_lang.game_locked);
        $('#multi_lockedp1').html(current_lang.multi_lockedp1);
        $('#multi_lockedp2').html(current_lang.multi_lockedp2);

          //Story End
        $('#story_pagetitle').html(current_lang.story_pagetitle);
        $('#end_pagetitle').html(current_lang.end_pagetitle);
        $('#c1_1').html(current_lang.c1_1);
        $('#c1_2').html(current_lang.c1_2);
        $('#c2_1').html(current_lang.c2_1);
        $('#c2_2').html(current_lang.c2_2);
        $('#c2_3').html(current_lang.c2_3);
        $('#text_end').html(current_lang.text_end);
        $('#text_end_tuto').html(current_lang.text_end_tuto);
        $('#text_end_lost').html(current_lang.text_end_lost);
        $('#texte_score').html(current_lang.text_score);
        $('#c1_3').html(current_lang.c1_3);
        $('#c2_4').html(current_lang.c2_4);
        $('#game_won').html(current_lang.game_won);
        $('#game_lost').html(current_lang.game_lost);
        $('#col_1').html(current_lang.col_1);
        $('#col_2').html(current_lang.col_2);
        $('#col_3').html(current_lang.col_3);
          //Game
        $('#you').attr('src', current_lang.you);
        $('#continue').html(current_lang.continue);
        $('#results').html(current_lang.results);
        $('#button_next').val(current_lang.continue);
        $('#history_name').html(current_lang.history_name);
        $('#conversations').html(current_lang.conversations);
        $('#anhearer_text').html(current_lang.anhearer_text);
        $('#anspeaker_text').html(current_lang.anspeaker_text);
        //$('#anabs_text').html(current_lang.anabs_text);
        $('#hearer_expl').html(current_lang.hearer_expl);
        $('#speaker_expl').html(current_lang.speaker_expl);
        $('#choice_words').html(current_lang.choice_words);
        $('#history_objects').html(current_lang.history_objects);
        $('#history_words').html(current_lang.history_words);
        $('#history_success').html(current_lang.history_success);
        $('#modal_title').html(current_lang.modal_title);
        $('#modal_body').html(current_lang.modal_body);
        $('#btn_yes').html(current_lang.btn_yes);
        $('#btn_no').html(current_lang.btn_no);

        //Feedback
        $('#speaker_success').html(current_lang.speaker_success);
        $('#speaker_learn').html(current_lang.speaker_learn);
        $('#speaker_failure').html(current_lang.speaker_failure);
        $('#hearer_success').html(current_lang.hearer_success);
        $('#hearer_learn').html(current_lang.hearer_learn);
        $('#hearer_failure').html(current_lang.hearer_failure);
        $('#tuto_hearer').html(current_lang.tuto_hearer);

        //Error Page

        $('#error_text').html(current_lang.error_text);
        $('#btn_home').html(current_lang.btn_home);
        $('#btn_continue').html(current_lang.btn_continue);

        //Info Page
        $('#infos_txt').html(current_lang.infos_txt);
        $('#infos_qu').html(current_lang.infos_qu);
        $('#infos_title').html(current_lang.infos_title);
        $('#question_title').html(current_lang.question_title);


        $('#label_q1').html(current_lang.label_q1);
        $('#label_q2').html(current_lang.label_q2);
        $('#label_q3').html(current_lang.label_q3);
        $('#label_q4').html(current_lang.label_q4);
        $('#label_q5').html(current_lang.label_q5);
        $('#label_q6').html(current_lang.label_q6);

        //Tooltips

        $('#id_code').attr('data-original-title',current_lang.tooltip_example);
        $('#best_scores').attr('data-original-title',current_lang.best_score);
        $('.mic').attr('data-original-title',current_lang.you);
        $('#lang').attr('data-original-title',current_lang.lang);
        $('#logoutbutton').attr('data-original-title',current_lang.logout);

        if (lang_str == 'fr'){
        $('#you_en').css('display','none');
        $('#you_fr').css('display','inline');
    } else {
        $('#you_fr').css('display','none');
        $('#you_en').css('display','inline');

    }
        //console.log(lang_str);


        $(document).prop('title', current_lang.title);
        //$('#title').html(lang.it[0].window_title);
        //$('text#button_next').val(lang.it[0].button_next);
        if ($('#anabs_text').attr('nb_skipped') == "1"){
          if (lang_str == "fr"){
            var replace_string = " conversation a eu lieu sans vous"
            $('#anabs_text').html(replace_string);
          }
          if (lang_str == "en"){
            var replace_string = " interaction happened whithout you"
            $('#anabs_text').html(replace_string);
          }
          if (lang_str == "it"){
            var replace_string = " "
            $('#anabs_text').html(replace_string);
          }
        } else {
          $('#anabs_text').html(current_lang.anabs_text);
        };

        //var interaction_string = current_lang.conversations + " " + $('#conversations').attr('nbr');
        //$('#conversations').html(interaction_string);


    Cookies.set('NamingGameLang',
        lang_str
        );
        $('html').attr('lang',lang_str);
        if (lang_str == "en"){$("#lang").attr("src",'../static/ng/img/english-flag.png').attr("value", "en");};
        //if (lang_str == "it"){$("#lang").attr("src",'../static/ng/img/italian-flag.png').attr("value","it");};
        if (lang_str == "fr"){$("#lang").attr("src",'../static/ng/img/french-flag.png').attr("value","fr");};

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


function switch_language(lang){
    var next_lang = "fr";
    if (lang == "fr"){next_lang = "en";
                      $("#lang").attr("src",'../static/ng/img/english-flag.png').attr("value", "en");
                    };
  //  if (lang == "en"){next_lang = "it";
    //                  $("#lang").attr("src",'../static/ng/img/italian-flag.png').attr("value","it");
    //                };
    //if (lang == "it"){next_lang = "fr";
    //                  $("#lang").attr("src",'../static/ng/img/french-flag.png').attr("value","fr");
    //                };

    if (lang == "en"){next_lang = "fr";
                        $("#lang").attr("src",'../static/ng/img/french-flag.png').attr("value","fr");
                      };
    Cookies.set('NamingGameLang',next_lang);
    return next_lang;
};


$(document).ready(function(){


      //  $.each(lang,function(key,value){

    $('#lang').click(function(event){
      //var sound_click = document.createElement('audio');
      //sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
      sound_click.play();
        change_language(switch_language($('#lang').attr('value')));
    });
//});



    // set_language();
});
