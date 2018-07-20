$(document).ready(function() {

var tuto = false;

if ($("#max_inter").text() == 10) {var game_mode="basic"};
if ($("#max_inter").text() == 50) {var game_mode="normal"};
var role = $("#role").text() ;
var context = $("#context").text() ;

if($('#ms').text() == 'None' || $('#mh').text() == 'None'){
	var success =  false;
	var learn = true;
} else {
	var success = $('#s').text();
	var learn = false;
}

var lang = $('html').attr('lang');




var src_logo_speaker = "../static/img/logo_speaker_temp.png" ;
var src_logo_hearer = "../static/img/logo_hearer_temp.png";


//Tooltips Game
if (lang == "fr"){
//Historique
$('#menu-h').tooltip({
	title : "Cliquez ici pour voir l'historique",
	placement : "bottom",
	trigger: "manual",
});

//Bouton info

/*if(game_mode=="basic"){
$('#info').tooltip({
	title : "Cliquez ici pour montrer les bulles d'aide",
	placement : "bottom",
	trigger : "hover focus",
});
} else {$('#info').tooltip({
	title : "Cliquez ici pour montrer les bulles d'aide",
	placement : "bottom",
	trigger : "manual",});}*/

//Abs Interaction
$('#anabs').tooltip({
	title: "Deux de vos camarades parlent sans que vous ne puissiez entendre leur conversation.",
	placement : "bottom",
	trigger: "manual",

});

//Speaker Role
$('#anspeaker').tooltip({
	title : "Faites deviner l'objet de votre choix à votre interlocuteur !",
	placement : "left",
	trigger: "manual",
});

//Hearer Role
$('#anhearer').tooltip({
	title : "Devinez ce dont votre interlocteur parle !",
	placement : "left",
	trigger: "manual",
});

//Avatar Others
$('#others').tooltip({
	title : "Votre moyen de communication avec vos partenaires !",
	placement : "right",
	trigger : "manual",
});


//Other Word
$('#other-word').tooltip({
	title : "Vous entendez ce mot :",
	placement : "top",
	trigger: "manual",
});

//Other Meaning "?"
$('#other-meaning').tooltip({
	title : "Voilà ce que votre interlocuteur voulait dire, vous vous en souviendrez pour la prochaine fois !",
	placement : "bottom",
	trigger: "manual",
});

$('#other-meaning').tooltip({
	title : "Votre interlocuteur ne connaissait pas ce mot mais il s'en souviendra pour la prochaine fois !",
	placement : "bottom",
	trigger: "manual",
});

} else if (lang == "en") {

	//Historique
	$('#menu-h').tooltip({
		title : "Click to see past interactions",
		placement : "bottom",
		trigger: "manual",
	});

	//Speaker Role
	$('#anspeaker').tooltip({
		title : "Try to make your partner guess an object !",
		placement : "left",
		trigger: "manual",
	});

	//Hearer Role
	$('#anhearer').tooltip({
		title : "Guess what your partner is talking about !",
		placement : "left",
		trigger: "manual",
	});

	//Avatar Others
	$('#others').tooltip({
		title : "Your medium of communication with your partners !",
		placement : "right",
		trigger : "manual",
	});


	//Other Word
	$('#other-word').tooltip({
		title : "You hear this word :",
		placement : "top",
		trigger: "manual",
	});

	//Other Meaning "?"
	$('#other-meaning').tooltip({
		title : "This is what your partner meant, you will remember it next time !",
		placement : "bottom",
		trigger: "manual",
	});

	$('#other-meaning').tooltip({
		title : "Your partner didn't know this word but they will remeber it next time !",
		placement : "bottom",
		trigger: "manual",
	});

} else if (lang == "it"){

	//Historique
	$('#menu-h').tooltip({
		title : "ITALIAN",
		placement : "bottom",
		trigger: "manual",
	});

	//Speaker Role
	$('#anspeaker').tooltip({
		title : "ITALIAN",
		placement : "left",
		trigger: "manual",
	});

	//Hearer Role
	$('#anhearer').tooltip({
		title : "ITALIAN",
		placement : "left",
		trigger: "manual",
	});

	//Avatar Others
	$('#others').tooltip({
		title : "ITALIAN",
		placement : "right",
		trigger : "manual",
	});


	//Other Word
	$('#other-word').tooltip({
		title : "ITALIAN",
		placement : "top",
		trigger: "manual",
	});

	//Other Meaning "?"
	$('#other-meaning').tooltip({
		title : "ITALIAN",
		placement : "bottom",
		trigger: "manual",
	});

	$('#other-meaning').tooltip({
		title : "ITALIAN",
		placement : "bottom",
		trigger: "manual",
	});

}


//Display Tooltips

	$('#menu-h').tooltip('show');

	$('#menu-h').click(function(){
		$('#menu-h').tooltip('hide')
	});

	$('#info').click(function(){
		$('#info').tooltip('hide')
	});

	$('#anabs').click(function(){
		$('#anabs').tooltip('hide')
	});

	$('#anspeaker').click(function(){
		$('#anspeaker').tooltip('hide')
	});

	$('#anhearer').click(function(){
		$('#anhearer').tooltip('hide')
	});

	$('#others').click(function(){
		$('#others').tooltip('hide')
	});

	$('#other-word').click(function(){
		$('#other-word').tooltip('hide')
	});

	$('#m5').click(function(){
		$('#m5').tooltip('hide')
	});


function hideTooltips(){
				$('#anabs').tooltip('hide');
				$('#m5').tooltip('hide');
				$('#anhearer').tooltip('hide');
				$('#anspeaker').tooltip('hide');
				$('#other-word').tooltip('hide');
				$('#other-meaning').tooltip('hide');
				$('#success').tooltip('hide');
				$('#failure').tooltip('hide');
				$('#learn').tooltip('hide');
			}



//Game loop function

if (context == "question" || context == "skipped") {

	//Update progress bar and title
	if(game_mode=="basic"){

		$('#info').css('color','gray');

	}


	//Setup depending on role
	if(role=='speaker') {

		if(tuto || game_mode=="basic"){$('#anspeaker').tooltip('show');};

	};

	if(role=='hearer') {

		/*if(newWord){
			$('#dont_know').css('display', 'inline-block');
			//"?"
			$('#m5').tooltip({
				title : "Vous pouvez cliquer ici si c'est la première fois que vous entendez ce mot",
				placement : "right",
			trigger: "manual",
			});
		}*/

		if(tuto || game_mode=="basic"){
			$('#anhearer').tooltip('show');
			$('#other-word').tooltip('show');
		/*	if(newWord){

				$('#m5').tooltip('show');
			} */

		};
	};

	if(context=='skipped') {

		if(tuto || game_mode=="basic"){$('#anabs').tooltip('show');};
	};

} else if (context == "result"){
		if (role=="speaker" || role=="hearer") {

			if(success) {

				//Tooltips
				if(role=="speaker"){//Feedback Success Speaker
					if (lang == 'fr'){
					$('#success').tooltip({
						title : "Bravo, votre interlocuteur vous a compris !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#success').tooltip({
						title : "Well done, your partner understood you !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#success').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

					if(game_mode == "basic" || tuto){$('#success').tooltip('show');}

				}else {//Feedback Success Hearer
					if (lang == 'fr'){
					$('#success').tooltip({
						title : "Bravo, vous avez compris votre interlocuteur ! Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#success').tooltip({
						title : "Well done, you understood your partner ! You will remember it next time !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#success').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

					if(game_mode == "basic" || tuto){$('#success').tooltip('show');}
					}
				$('#success').click(function(){
					$('#success').tooltip('hide')
				});



			} else if (learn) {
				/*$('#failure').css('display', 'none').css('visibility', 'hidden');
				$('#success').css('display', 'none').css('visibility', 'hidden');
				$('#learn').css('display', 'block').css('visibility', 'visible');*/
				if(role=="speaker") {
					if (lang == 'fr'){
					$('#learn').tooltip({
						title : "Votre interlocuteur ne connaissait pas ce mot mais s'en souviendra pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#learn').tooltip({
						title : "Your partner didn't know this word but will remember it next time !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#learn').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

					if(game_mode == "basic" || tuto){$('#learn').tooltip('show');}
					$('#learn').click(function(){
						$('#learn').tooltip('hide')
					});
				} else {
					if (lang == 'fr'){
					$('#other-meaning').tooltip({
						title : "Voilà ce que voulait dire votre interlocuteur. Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#other-meaning').tooltip({
						title : "This what your partner meant. You will remember it next time !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#other-meaning').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

					if(game_mode == "basic" || tuto){$('#other-meaning').tooltip('show');}
					$('#other-meaning').click(function(){
						$('#other-meaning').tooltip('hide')
					});
				}



			} else{
				/*$('#failure').css('display', 'block').css('visibility', 'visible');
				$('#success').css('display', 'none').css('visibility', 'hidden');
				$('#learn').css('display', 'none').css('visibility', 'hidden');*/

				if(role=="speaker"){ //Feedback Failure Speaker
					if (lang == 'fr'){
					$('#failure').tooltip({
						title : "Dommage, votre interlocuteur pensait que vous parliez d'autre chose. Il s'en souviendra pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#failure').tooltip({
						title : "Too bad, your partner thought you were talking about something else. They will remember it next time !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#failure').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

				}else { //Feedback Failure Hearer
					if (lang == 'fr'){
					$('#failure').tooltip({
						title : "Dommage, votre interlocuteur voulait parler d'autre chose. Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'en'){
					$('#failure').tooltip({
						title : "Too bad, your partner meant something else. You will remember it next time !",
						placement : "right",
						trigger: "manual",
					});
				} else if (lang == 'it'){
					$('#failure').tooltip({
						title : "ITALIAN",
						placement : "right",
						trigger: "manual",
					});
				}

					if(game_mode == "basic" || tuto){$('#failure').tooltip('show');}
				}
				$('#failure').click(function(){
					$('#failure').tooltip('hide')
				});
			}
		};
}

//Info Button


	function showTooltips(){
		$('#anabs').tooltip('show');
		$('#m5').tooltip('show');
		$('#anhearer').tooltip('show');
		$('#anspeaker').tooltip('show');
		$('#other-word').tooltip('show');
		$('#other-meaning').tooltip('show');
		$('#success').tooltip('show');
		$('#failure').tooltip('show');
		$('#learn').tooltip('show');
	}

	/*$('#info').click(function(){
		if (game_mode == "normal"){
			//$('#info').tooltip('destroy');
			if(tuto){
				tuto=false;
				$('#info').css('color', 'white');
				//hideTooltips();
			}else{
				tuto=true;
				$('#info').css('color', '#AF59D4');
				//showTooltips();
			}
		}
	});*/

});
