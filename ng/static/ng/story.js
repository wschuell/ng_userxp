
if(mode=="end"){
	//Interroger serveur pour savoir si jeu normal ou tuto
	//var game_type ="tuto"; //Valeurs possibles : "tuto" et "normal"
	$('#page_title_end').css('display', 'block');
	$('#story_pagetitle').css('display', 'none');
	$('#picture2').css('display', 'none');
	$('#picture').css('display', 'block');
	$('#cbot').css('display', 'none');
	$('.c1').css('display', 'none');
	$('.c2').css('display', 'none');
	$('#text_end').css('display', 'block');
	$('#score_text').css('display', 'none');


	$('.continue').click(function(){
		sound_click.play();
		if($('#text_end').css('display')=='block'){
			$('#score_text').css('display', 'block');
			$('#picture').css('display', 'none');
			$('#picture2').css('display', 'block');
			$('#text_end').css('display', 'none');
		} else {
			/*window.location.href = "game_tutorial";*/
			$(this).prop('disable',true);
    			$("html").addClass("wait");
					window.location.href='/';
			}
	});


} else if (mode=="story"){
	$('#score_text').css('display', 'none');
	$('#text_end').css('display', 'none');
	$('#page_title_end').css('display', 'none');
	$('#story_pagetitle').css('display', 'block');
	$('#picture').css('display', 'block');
	$('#picture2').css('display', 'none');
	$('#cbot').css('display', 'block');
	$('.c1').css('display', 'block');
	$('.c2').css('display', 'none');

	$('.continue').click(function(){
		if($('.c1').css('display')=='block'){
			$('.c2').css('display', 'block');
			$('.c1').css('display', 'none');
		} else {
			/*window.location.href = "game_tutorial";*/
			$(this).prop('disable',true);
    			$("html").addClass("wait");
					window.location.href='/new_experiment/basic';
			}
	});
};


//Menu

//Sound
$('#sound-off').click(function(){
	sound_click.play();
	$('#sound-off').css('display','none');
	$('#sound-on').css('display','inline');
});
$('#sound-on').click(function(){
	sound_click.play();
	$('#sound-on').css('display','none');
	$('#sound-off').css('display','inline');
});
//Home
$('#home').click(function(){
	sound_click.play();
	$("#myModal").modal({
		keyboard : true,
	});
});



var sound_click = document.createElement('audio');

$(document).ready(function(){
	$('body').css('visibility', 'visible');

if (typeof Cookies.get('NamingGameSound') === 'undefined'){
	Cookies.set('NamingGameSound', true);
	sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
	$('#sound-on').css('display','none');
	$('#sound-off').css('display','inline');
} else if (Cookies.get('NamingGameSound')) {
	sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
	$('#sound-on').css('display','none');
	$('#sound-off').css('display','inline');
} else {
 sound_click.setAttribute('src', "");
 $('#sound-off').css('display','none');
 $('#sound-on').css('display','inline');
}

	//Tooltips

	if ($('html').attr('lang') == 'fr'){
	$('#1.0').tooltip({
		title : "Objets",
		placement : "left",
		trigger: "hover focus",
	});
	$('#2.0').tooltip({
		title : "Mots préférés",
		placement : "left",
		trigger: "hover focus",
	});
	$('#3.0').tooltip({
		title : "Seconds mots préférés s'il y en a",
		placement : "left",
		trigger: "hover focus",
	});
	} else if ($('html').attr('lang') == 'en'){
		$('#1.0').tooltip({
			title : "Objets",
			placement : "left",
			trigger: "hover focus",
		});
		$('#2.0').tooltip({
			title : "Mots préférés",
			placement : "left",
			trigger: "hover focus",
		});
		$('#3.0').tooltip({
			title : "Seconds mots préférés s'il y en a",
			placement : "left",
			trigger: "hover focus",
		});
	} else {
		$('#1.0').tooltip({
			title : "ITALIAN",
			placement : "left",
			trigger: "hover focus",
		});
		$('#2.0').tooltip({
			title : "ITALIAN",
			placement : "left",
			trigger: "hover focus",
		});
		$('#3.0').tooltip({
			title : "ITALIAN",
			placement : "left",
			trigger: "hover focus",
		});
	}
		$('#1.0').tooltip("show");
		$('#2.0').tooltip("show");
		$('#3.0').tooltip("show");
});
