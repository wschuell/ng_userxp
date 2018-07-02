$(document).ready(function() {

var tuto = false;
var game = true;
var firstGame = false; //Interaction serveur : Demander si Tutoriel
var i = 1;



var src_logo_speaker = "../static/img/logo_speaker_temp.png" ;
var src_logo_hearer = "../static/img/logo_hearer_temp.png";

//Remplacer par les bons meanings
var m0 = "<img src='../static/img/meaning_temp.png'class='img-responsive m'>";
var m1 = "<img src='../static/img/avatar_player_default.jpg'class='img-responsive m'>";
var m2 = "<img src='../static/img/radio.png'class='img-responsive m'>";
var m3 = "<img src='../static/img/history.png'class='img-responsive m'>";
var m4 = "<img src='../static/img/logo_abs_temp.png'class='img-responsive m'>";
var m5 = "<img src='../static/img/question-mark.png'class='img-responsive m'>";

//Interaction serveur : Mots proposés pour la partie
var w0 = "rowuwi";
var w1 = "W1";
var w2 = "W2";
var w3 = "W3";
var w4 = "W4";
var w5 = "W5";

$('#m0').after(m0);
$('#m1').after(m1);
$('#m2').after(m2);
$('#m3').after(m3);
$('#m4').after(m4);
$('#m5').after(m5);




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



//Tooltips Game

//Historique
$('#menu-h').tooltip({
	title : "Cliquez ici pour voir l'historique",
	placement : "bottom",
	trigger: "manual",	
});

//Bouton info

if(!firstGame){
$('#info').tooltip({
	title : "Cliquez ici pour montrer les bulles d'aide",
	placement : "bottom",
	trigger : "hover focus",
});
} else {$('#info').tooltip({
	title : "Cliquez ici pour montrer les bulles d'aide",
	placement : "bottom",
	trigger : "manual",});}

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

function run(){
	// Interaction serveur : Demander rôle + mot choisi et s'il a déjà été vu si hearer
	var role = "hearer"; //Possible values : "speaker", "hearer" and "abs"
	var otherWord = "W2"; //Mot hearer temporaire
	var newWord = true;

	//Uncheck radio buttons when script starts
	$('.mradio').find('label').removeClass('active').end().find('[type="radio"]').prop('checked', false);

	$('.wradio').find('label').removeClass('active').end().find('[type="radio"]').prop('checked', false);

	//Update progress bar and title
	if(firstGame){
		$('#conversations').text("Conversation "+i+ "/10");
		var iUpdate = 10;
		$('#info').css('color','gray');
		
	}else{
		$('#conversations').text("Conversation "+i+ "/50");
		var iUpdate = 2;
	};
	var newi = i*iUpdate;
	$(".progress-bar").attr('aria-valuenow', newi+"%");
	$(".progress-bar").css('width', newi+"%");

	//Change "continue" button
	$('#next').css('display','none');
	$('#continue').css('display','block').addClass('disabled').prop('disabled',true);
	

	//Setup depending on role
	if(role=='speaker') {
		
		if(tuto || firstGame){$('#anspeaker').tooltip('show');};
		//Annonce rôle
		$('#anspeaker').css('visibility','visible').css('display','block');
		$('#anhearer').css('visibility','hidden').css('display','none');
		$('#anabs').css('visibility','hidden').css('display','none');

		//Logos S/H
		$('#role_player').attr('src', src_logo_speaker);
		$('#role_others').attr('src', src_logo_hearer);

		//Choice Bubble
		$('.speaker').css('visibility','visible').css('display','block');
		$('.hearer').css('visibility','hidden').css('display','none');
		$('.meanings').css('visibility','visible').css('display','block');

		//Bubbles
		$('#word1').text('...');
		$('#you-word').css('visibility','visible').css('display','block');
		$('#you-meaning').css('visibility','hidden').css('display','block');
		$('#other-word').css('visibility','hidden').css('display','block');
		$('#other-meaning').css('visibility','hidden').css('display','block');	
	};

	if(role=='hearer') {
		
		//Annonce rôle
		$('#anhearer').css('visibility','visible').css('display','block');
		$('#anspeaker').css('visibility','hidden').css('display','none');
		$('#anabs').css('visibility','hidden').css('display','none');

		//Logos S/H
		$('#role_player').attr("src", src_logo_hearer);
		$('#role_others').attr("src", src_logo_speaker);

		//Choice Bubble
		$('.hearer').css('visibility','visible').css('display','block');
		$('.speaker').css('visibility','hidden').css('display','none');
		$('.meanings').css('visibility','visible').css('display','block');

		//Bubbles
		
		$('#you-word').css('visibility','hidden').css('display','block');
		$('#you-meaning').css('visibility','hidden').css('display','block');
		$('#other-meaning').css('visibility','hidden').css('display','block');		
		$('#other-word').css('visibility','visible').css('display','block');
		$('#word2').text(otherWord);
		
		if(newWord){
			$('#dont_know').css('display', 'inline-block');
			//"?"
			$('#m5').tooltip({
				title : "Vous pouvez cliquer ici si c'est la première fois que vous entendez ce mot",
				placement : "right",
			trigger: "manual",
			});
		}
		
		if(tuto || firstGame){
			$('#anhearer').tooltip('show');
			$('#other-word').tooltip('show');
			if(newWord){
				
				$('#m5').tooltip('show');
			}
			
		};
	};

	if(role=='abs') {

		if(tuto || firstGame){$('#anabs').tooltip('show');};
		//Annonce rôle
		$('#anabs').css('visibility','visible').css('display','block');
		$('#anhearer').css('visibility','hidden').css('display','none');
		$('#anspeaker').css('visibility','hidden').css('display','none');

		//Logos S/H
		$('#role_player').attr('src', '');
		$('#role_others').attr('src', '');

		//Choice Bubble
		$('.speaker').css('visibility','hidden').css('display','none');
		$('.hearer').css('visibility','hidden').css('display','none');
		$('.meanings').css('visibility','hidden').css('display','block');

		//Bubbles
		$('#you-word').css('visibility','hidden').css('display','block');
		$('#you-meaning').css('visibility','hidden').css('display','block');
		$('#other-word').css('visibility','hidden').css('display','block');
		$('#other-meaning').css('visibility','hidden').css('display','block');	

		//Btn continuer
		$('#continue').removeClass('disabled').prop('disabled',false);
	};


	


	//Display Game History
	$("#menu-h").popover({
		placement : 'bottom',
        	html : true,
        	content: function() {
        		return $('#popover-body').html();
       		},
		title: function() {
          		return $('#popover-heading').html();
      		},
	});

	
	

	//Update Bubbles Choice Meaning / Words Speaker and hearer
	$('.m').unbind().click(function(){		
		var mSelected = $(this).clone().removeClass('m').addClass('meaning');
		$('#you-meaning').css('visibility', 'visible').css('display','block');
		$('#you-meaning').html(mSelected);
		if(role=="speaker") {
			$('.speaker-words').css('visibility', 'visible').css('display','block');
		} else {
			$('#continue').removeClass('disabled').prop('disabled',false);
			$('#other-word').tooltip('hide');
			$('#anhearer').tooltip('hide');
			$('#m5').tooltip('hide');
		};
	});
	
	$('.w').unbind().click(function(){
		var wSelected = $(this).text();
		$('#word1').text(wSelected);
		$('#continue').removeClass('disabled').prop('disabled',false);
		$('#anspeaker').tooltip('hide');
	});

	//Select choice
	$('#continue').unbind().click(function(){

				//Interaction serveur : Envoyer choix joueur + recevoir feedback (ok ou apprentissage +meaning)
		
		var okMeaning = m4; //Temporaire
		var success = true; //Temporaire
		var learn = false; //Temporaire

		if (role=="speaker" || role=="hearer") {
			$('.meanings').css('visibility', 'hidden').css('display', 'none');
			$('#speaker-expl').css('display', 'none');
			$('.speaker-words').css('visibility', 'hidden').css('display', 'none');
			$('.feedback').css('display', 'block').css('visibility', 'visible');	
			$('#other-meaning').css('visibility', 'visible').css('display', 'block');
			$('#other-meaning').html(okMeaning);
			$('#other-meaning img').css("border", "none");
			$('.expl').css('visibility','hidden').css('display','none');
		
		

			if(success) {
				$('#success').css('display', 'block').css('visibility', 'visible');
				$('#failure').css('display', 'none').css('visibility', 'hidden');
				$('#learn').css('display', 'none').css('visibility', 'hidden');
				//Tooltips
				if(role=="speaker"){//Feedback Success Speaker
					$('#success').tooltip({
						title : "Bravo, votre interlocuteur vous a compris !",
						placement : "right",
						trigger: "manual",
					});
					if(firstGame || tuto){$('#success').tooltip('show');}
			
				}else {//Feedback Success Hearer
					$('#success').tooltip({
						title : "Bravo, vous avez compris votre interlocuteur ! Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
					if(firstGame || tuto){$('#success').tooltip('show');}
					}
				$('#success').click(function(){
					$('#success').tooltip('hide')
				});

				

			} else if (learn) {
				$('#failure').css('display', 'none').css('visibility', 'hidden');
				$('#success').css('display', 'none').css('visibility', 'hidden');
				$('#learn').css('display', 'block').css('visibility', 'visible');
				if(role=="speaker") {
					$('#learn').tooltip({
						title : "Votre interlocuteur ne connaissait pas ce mot mais s'en souviendra pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
					if(firstGame || tuto){$('#learn').tooltip('show');}
					$('#learn').click(function(){
						$('#learn').tooltip('hide')
					});
				} else {
					$('#other-meaning').tooltip({
						title : "Voià ce que voulait dire vote interlocuteur. Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
					if(firstGame || tuto){$('#other-meaning').tooltip('show');}
					$('#other-meaning').click(function(){
						$('#other-meaning').tooltip('hide')
					});
				}
			
			

			} else{
				$('#failure').css('display', 'block').css('visibility', 'visible');
				$('#success').css('display', 'none').css('visibility', 'hidden');
				$('#learn').css('display', 'none').css('visibility', 'hidden');
				
				if(role=="speaker"){//Feedback Failure Speaker
					$('#failure').tooltip({
						title : "Dommage, votre interlocuteur pensait que vous parliez d'autre chose. Il s'en souviendra pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
					
			
				}else {//Feedback Failure Hearer
					$('#failure').tooltip({
						title : "Dommage, votre interlocuteur voulait parler d'autre chose. Vous vous en souviendrez pour la prochaine fois !",
						placement : "right",
						trigger: "manual",
					});
					if(firstGame || tuto){$('#failure').tooltip('show');}
				}
				$('#failure').click(function(){
					$('#failure').tooltip('hide')
				});
				
				
			
			
			};

			$('#next').css('display','block').removeClass('disabled').prop('disabled',false);
			$('#continue').css('display','none');


			//++Update history
			if(role=="hearer"){
				var newHImg = $('#other-meaning').html();
				var newHWord = $('#other-word').text();
				if(success){
					$('#popover-body').append("<div class='row' id='nameCol"+i+"'><div class='col-xs-3' >"+ newHImg + "</div><div class='col-xs-6' ><p class='w-histo'>"+newHWord+"</p></div><div class='col-xs-3' ><img src='../static/img/feedback_success_temp.png'class='img-responsive meaning'class='img-responsive img-histo'></div></div>");
				} else {
					$('#popover-body').append("<div class='row'id='nameCol"+i+"'><div class='col-xs-4' >"+ newHImg + "</div><div class='col-xs-4' ><p class='w-histo'>"+newHWord+"</p></div><div class='col-xs-4' ></div></div>");};

				var col = '#nameCol'+i + " img";

				$(col).addClass("img-histo").removeClass("meaning");

			};	
	
		}; 
	});
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

	$('#info').click(function(){
		if (!firstGame){
			//$('#info').tooltip('destroy');
			if(tuto){
				tuto=false;
				$('#info').css('color', 'white');
				hideTooltips();
			}else{
				tuto=true;
				$('#info').css('color', '#AF59D4');
				showTooltips();
			}
		}	
	});

run();



$('#next').click(function(){
		i=i+1;
		
		if(firstGame && i>10) {game=false;
			$('#next').click(function(){window.location.href = "story.html";});
		} else if(i>50){
			game=false;
			$('#next').click(function(){window.location.href = "story.html";});
		}else {
			$('.feedback').css('display', 'none').css('visibility', 'hidden');
			$('.speaker-words').css('display', 'block');
			hideTooltips();	
			run();
			
		};
			
	});




});
