
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
	$('#sound-off').css('display','none');
	$('#sound-on').css('display','inline');
});
$('#sound-on').click(function(){
	$('#sound-on').css('display','none');
	$('#sound-off').css('display','inline');
});
//Home
$('#home').click(function(){
	$("#myModal").modal({
		keyboard : true,
	});
});


$(document).ready(function(){
	$('body').css('visibility', 'visible');
});
