
    var sound_click = document.createElement('audio');
    var music = document.createElement('audio');

    if (typeof Cookies.get('NamingGameSound') === 'undefined'){
        Cookies.set('NamingGameSound', true);
        sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
        music.setAttribute('src', "{% static 'ng/sounds/263479__orangefreesounds__dreamy-melodic-synth-loop.wav' %}");

     $('#sound-on').css('display','none');
     $('#sound-off').css('display','inline');
    } else if (Cookies.get('NamingGameSound')) {
       sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
       music.setAttribute('src', "{% static 'ng/sounds/263479__orangefreesounds__dreamy-melodic-synth-loop.wav' %}");

     $('#sound-on').css('display','none');
     $('#sound-off').css('display','inline');
    } else {
      sound_click.setAttribute('src', "{% static 'ng/sounds/silence.wav' %}");
      music.setAttribute('src', "{% static 'ng/sounds/silence.wav' %}");

      $('#sound-off').css('display','none');
      $('#sound-on').css('display','inline');
    }

    //Sound
    $('#sound-off').click(function(){
      Cookies.set('NamingGameSound', true);
      sound_click.setAttribute('src', "{% static 'ng/sounds/silence.wav' %}");
      music.setAttribute('src', "{% static 'ng/sounds/silence.wav' %}");
     $('#sound-off').css('display','none');
     $('#sound-on').css('display','inline');
    });
    $('#sound-on').click(function(){
      Cookies.set('NamingGameSound', false);
      sound_click.setAttribute('src', "{% static 'ng/sounds/60945__erh__click.wav' %}");
      music.setAttribute('src', "{% static 'ng/sounds/263479__orangefreesounds__dreamy-melodic-synth-loop.wav' %}");
      // sound_click.play();
     $('#sound-on').css('display','none');
     $('#sound-off').css('display','inline');
    });
