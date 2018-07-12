//LANG GETS DECLARED HERE, this line is used in the python script generating it
var lang = {"fr": {"game_locked": "Terminer le Tutoriel pour débloquer", "speaker_expl": "De quoi voulez vous parler ?", "comment_avatar": "C'est vous !", "continue": "Continuer", "button_basic": "Tutoriel", "enter_player_name": "Entrez votre nom ici :", "welcome": "Le Naming Game !", "button_multi": "Multijoueur", "history_success": "Succès", "history_words": "Mots", "c2_4": "Mais attention, vous n'avez à vous tous qu'un <span class='important'>nombre limité de conversations</span> pour réussir !", "window_title": "Le Naming Game", "c2_2": "L'un de vous proposera un mot et l'autre devra deviner l'objet auquel il fait référence.", "scores_title": "Meilleurs Scores", "btn_yes": "Oui, quitter la partie", "home_pagetitle": "Accueil", "anhearer": "On vous parle !", "hearer_expl": "De quoi vous parle-t-on ?", "text_score": "Votre score est de ", "anabs": "conversations ont eu lieu en votre absence", "conversations": "Conversation", "button_normal": "Jeu", "history_name": "Historique", "button_next": "Continuer", "btn_no": "Non, continuer la partie", "choice_words": "Quel mot voulez-vous utiliser ?", "story_pagetitle": "Histoire", "end_pagetitle": "Félicitations !", "c2_3": "Parfois vous proposerez un mot, parfois vous devinerez l'objet et parfois encore vous ne ferez pas partie de la conversation et ne saurez pas ce qui s'y est dit.", "c1_1": " Vous avez été enlevé par des Extraterrestres !", "label_lang": "Choisissez le langue du jeu :", "c1_3": "<span class=\"important\">Aucun de vous ne parle la m\u00eame langue</span> mais vous voulez tous vous échapper pour pouvoir rentrer chez vous.", "c1_2": "Vous voilà enfermé seul dans une pièce de leur vaisseau. Dans les pièces d'à côté se trouvent <span class='important'>4 autres individus</span> que vos ravisseurs ont également enlevés aux quatre coins de la galaxie.", "history_objects": "Objets", "text_end": "Après avoir réussi à vous comprendre, vous mettez au point un plan d'évasion spectaculaire. Vos ravisseurs ne voient rien venir avant qu'il ne soit trop tard. Vous leur volez un vaisseau qu'un de vos camarades pilote pour vous ramener tous paisiblement chez vous.", "modal_body": "Si vous quittez la partie en cours, celle-ci ne sera pas sauvegardée et vos données ne pourront pas être utilisées. Voulez-vous toujours quitter ?", "label_code": "Si vous avez un code spécial, entrez le ici :", "c2_1": "Pour ce faire, vous ne pourrez parler que <span class='important'>deux par deux</span> grâce à une <span class='important'>radio</span>, <span class='important'>sans savoir lequel de vos camarades d'infortune est à l'autre bout</span>.", "multi_locked": "Terminer le Jeu 5 fois pour débloquer", "anspeaker": "C'est à vous de parler !"}, "en": {"game_locked": "Complete the Tutorial to unlock", "speaker_expl": "What do you want to talk about ?", "comment_avatar": "That's you !", "continue": "Continue", "button_basic": "Tutorial", "enter_player_name": "Enter your name here :", "welcome": "The Naming Game!", "button_multi": "Multiplayer", "history_success": "Succes", "history_words": "Words", "c2_4": "But careful, you only have a <span class=\"important\">limited number of conversations</span> to succed\u00a0!", "window_title": "The Naming Game", "c2_2": "One of you will say a word and the other will have to guess which object he is referring to.", "scores_title": "Best Scores", "btn_yes": "Yes, quit the game", "home_pagetitle": "Home", "anhearer": "Someone is talking to you\u00a0!", "hearer_expl": "What does it means ?", "text_score": "Your score is ", "anabs": "interactions happened without you being a part of it.", "conversations": "Interaction", "button_normal": "Game", "history_name": "Past Interactions", "button_next": "Continue", "btn_no": "No, resume the game", "choice_words": "Quel mot voulez-vous utiliser ?", "story_pagetitle": "Story", "end_pagetitle": "Congratulations !", "c2_3": "Sometimes you will talk, sometimes you will guess and sometimes you won't be in the conversation and you won't know what was said.", "c1_1": " You have been kidnapped by Aliens !", "label_lang": "Choose the game language :", "c1_3": "<span class=\"important\"><span class=\"important\">None of you is from the same planet or speak the same language</span> but you all want the same thing\u00a0: escape and go back home.", "c1_2": "Now, you are locked alone in a room of their huge spaceship. In the rooms next to yours, there are <span class=\"important\">3 other individuals</span> also kidnapped by your abductors at the four corners of the galaxy.", "history_objects": "Objects", "text_end": "Once you managed to understand each other, you develop a spectacular escape plan. Your abductors don't even see it coming until it's too late. You steal a ship from them and one of your companions drive you back home with it.", "modal_body": "If you quit the ongoing game, it won't be saved and your data won't help us. Do you still want to quit\u00a0?", "label_code": "If you have a special code, enter it here :", "c2_1": "To do so, you may only talk <span class=\"important\">by pairs</span> thanks to a <span class=\"important\">radio</span>, <span class=\"important\">without knowing wich one of your companions in misery is on the other side</span>.", "multi_locked": "Complete the Game 5 times to unlock", "anspeaker": "Your turn to speak\u00a0!"}, "it": {"game_locked": "", "speaker_expl": "", "comment_avatar": "", "continue": "", "button_basic": "", "enter_player_name": "", "welcome": "Il Naming Game !", "button_multi": "", "history_success": "", "history_words": "", "c2_4": "", "window_title": "Il Naming Game", "c2_2": "", "scores_title": "Wall of Fame", "btn_yes": "", "home_pagetitle": "", "anhearer": "", "hearer_expl": "", "text_score": " ", "anabs": "", "conversations": "", "button_normal": "", "history_name": "", "button_next": "", "btn_no": "", "choice_words": "", "story_pagetitle": "", "end_pagetitle": "", "c2_3": "", "c1_1": " ", "label_lang": "", "c1_3": "", "c1_2": "", "history_objects": "", "text_end": " ", "modal_body": "", "label_code": "", "c2_1": "", "multi_locked": "", "anspeaker": ""
}};
//LANG GETS DECLARED HERE, this line is used in the python script generating it



    function change_language(lang_str){
        var current_lang = lang[lang_str];
        $('#window_title').html(current_lang.window_title);
        $('#welcome').html(current_lang.welcome);
        $('#enter_player_name').html(current_lang.enter_player_name);
        $('#label_lang').html(current_lang.label_lang);
        $('#label_code').html(current_lang.label_code);

          //Home
        $('#scores_title').html(current_lang.scores_title);
        $('#button_basic').html(current_lang.button_basic);
        $('#button_multi').html(current_lang.button_multi);
        $('#button_normal').html(current_lang.button_normal);
        $('#comment_avatar').html(current_lang.comment_avatar);
        $('#home_pagetitle').html(current_lang.home_pagetitle);
        $('#game_locked' ).html(current_lang.game_locked);
        $('#multi_locked').html(current_lang.multi_locked);

          //Story End
        $('#story_pagetitle').html(current_lang.story_pagetitle);
        $('#end_pagetitle').html(current_lang.end_pagetitle);
        $('#c1_1').html(current_lang.c1_1);
        $('#c1_2').html(current_lang.c1_2);
        $('#c2_1').html(current_lang.c2_1);
        $('#c2_2').html(current_lang.c2_2);
        $('#c2_3').html(current_lang.c2_3);
        $('#text_end').html(current_lang.text_end);
        $('#text_score').html(current_lang.text_score);
        $('#c1_3').html(current_lang.c1_3);
        $('#c2_4').html(current_lang.c2_4);
          //Game
        $('#button_next').html(current_lang.button_next);
        $('#continue').html(current_lang.continue);
        $('#history_name').html(current_lang.history_name);
        $('#conversations').html(current_lang.conversations);
        $('#anhearer').html(current_lang.anhearer);
        $('#anspeaker').html(current_lang.anspeaker);
        $('#anabs').html(current_lang.anabs);
        $('#hearer_expl').html(current_lang.hearer_expl);
        $('#speaker_expl').html(current_lang.speaker_expl);
        $('#choice_words').html(current_lang.choice_words);
        $('#history_objects').html(current_lang.history_objects);
        $('#history_words').html(current_lang.history_words);
        $('#history_success').html(current_lang.history_success);
        $('#modal_body').html(current_lang.modal_body);
        $('#btn_yes').html(current_lang.btn_yes);
        $('#btn_no').html(current_lang.btn_no);


        console.log(current_lang.button_multi);


        $(document).prop('title', current_lang.title);
        //$('#title').html(lang.it[0].window_title);
        //$('text#button_next').val(lang.it[0].button_next);
        if ($('#not_involved').attr('nb_skipped') && $('#not_involved').attr('nb_skipped') != "1"){
            var replace_string = "" + $('#not_involved').attr('nb_skipped') + current_lang.not_involved_post;
            $('#not_involved').html(replace_string);
        };


    Cookies.set('NamingGameLang',
        lang_str
        );
        $('html').attr('lang',lang_str);
        if (lang_str == "en"){$("#lang").attr("src",'../static/ng/img/english-flag.png').attr("value", "en");};
        if (lang_str == "it"){$("#lang").attr("src",'../static/ng/img/italian-flag.png').attr("value","it");};
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
    var next_lang = "";
    if (lang == "fr"){next_lang = "en";
                      $("#lang").attr("src",'../static/ng/img/english-flag.png').attr("value", "en");
                    };
    if (lang == "en"){next_lang = "it";
                      $("#lang").attr("src",'../static/ng/img/italian-flag.png').attr("value","it");
                    };
    if (lang == "it"){next_lang = "fr";
                      $("#lang").attr("src",'../static/ng/img/french-flag.png').attr("value","fr");
                    };
    return next_lang;
};


$(document).ready(function(){


        $.each(lang,function(key,value){

    $('#lang').click(function(event){
        var language = $(this).val();
        var next = switch_language(language);
        change_language(next);
    });
});



    set_language();
}
    );
