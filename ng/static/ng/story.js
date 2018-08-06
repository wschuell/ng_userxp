
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

};
