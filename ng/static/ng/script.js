$( document ).ready(function() {
  $.ajaxPrefilter( function(options, originalOptions, jqXHR) {
    jqXHR.setRequestHeader('X-CSRF-Token', Cookies.get('csrftoken'));
  });

  $(document).ajaxStart(function () {
    $("html").addClass("wait");
  });
  $(document).ajaxStop(function () {
    $("html").removeClass("wait");
  });

  //$("#word_speaker").hide();
  $("#button_next, #button_start").click(function(){
    $("#button_next, #button_start").addClass('disabled');
    $("html").addClass("wait");
    window.location.href = url_continue ;}
  );
  //select meanings and words

  $("#continue").addClass('disabled');

  /* $('#meaning_inner.meaning_img').click(function(event){
    //$("#word_speaker").show();

    if (! $('html').hasClass('wait')) {
      if(! $(this).hasClass('selected_m')) {
        $(".selected_m").removeClass("selected_m");
        $(this).addClass("selected_m");

        if ($(".selected_w").length > 0) {
          $("#continue.interact_speaker").removeClass('disabled');
        };
        $("#continue.interact_hearer").removeClass('disabled');
      } else {
        $(this).removeClass("selected_m");
        $("#continue").addClass('disabled');
      };
    }
  });

  $('.word_text_speaker').click(function(event){
    if (! $('html').hasClass('wait')) {
      if (! $(this).hasClass('selected_w')) {
        $(".selected_w").removeClass("selected_w");
        $(this).addClass('selected_w');
        if ($(".selected_m").length > 0) {
          $("#continue").removeClass('disabled');
        };
      } else {
        $(this).removeClass("selected_w");
        $("#continue").addClass('disabled');
      };
    }
  });*/

  //interact button with ajax
/*  $("#continue.interact_hearer").click(function(event){
    if($('.selected_m')[0] == undefined && !$("#continue").hasClass('disabled') ) {
      $("#continue").addClass('disabled');
    // $.ajax({
    //   url: url_results_hearer_base + $(".selected_m").attr("meaning_name") + "/results_json/",
    //   success: function (result) {
    //     var result_json = JSON.parse(result);
    //     $.ajax({
    //       url: url_results_inner_base  + result_json.bool_succ,
    //       success: function (result2) {
    //         $("#choose").html(result2);
    //         set_language();
    //       }
    //     });
    //   }
    // });
     window.location.href=url_results_hearer_base + $(".selected_m").attr("meaning_name") + "/results_continue/"}
     return false;
  });

  $("#continue.interact_speaker").click( function (event) {
    if($('.selected_m')[0] == undefined && $('.selected_w')[0] == undefined && !$("#continue").hasClass('disabled') ){
      $("#continue").addClass('disabled');
    // $.ajax({
    //   url: url_results_speaker_base + $(".selected_m").attr("meaning_name") + "-" + $(".selected_w").attr("word_name") + "/results_json/",
    //   success: function (result) {
    //     var result_json = JSON.parse(result);
    //     $.ajax({
    //       url: url_results_inner_base  + result_json.bool_succ,
    //       success: function (result2) {
    //         $("#choose").html(result2);
    //        set_language();
    //       }
    //     });
    //   }
    // });
      window.location.href=url_results_speaker_base + $(".selected_m").attr("meaning_name") + "-" + $(".selected_w").attr("word_name") + "/results_continue/"}
      return false;
  }); */

  //buttons
  $("#homebutton").click(function(){
    $("html").addClass("wait");
    window.location.href="/";
  });

  $("#logoutbutton").click(function(){
    $("html").addClass("wait");
    window.location.href=url_logout;
  });

  $("#new_xp_button").click(function(){
    $(this).prop('disable',true);
    $("html").addClass("wait");
    window.location.href='/choose_experiment';
  });

  $("#button_basic").click(function(){
    $(this).prop('disable',true);
    $("html").addClass("wait");
    window.location.href='/new_experiment/basic';
  });
  $("#button_normal").click(function(){
    $(this).prop('disable',true);
    $("html").addClass("wait");
    window.location.href='/new_experiment/normal';
  });
  $("#button_multi").click(function(){
    $(this).prop('disable',true);
    $("html").addClass("wait");
    window.location.href='/new_experiment/multiuser';
  });

  //username
  var user_str = Cookies.get('NamingGameUser');
   $("#username").html(user_str);
   $(document).ajaxStop(function () {
   $("#username").html(user_str);
  });
});
