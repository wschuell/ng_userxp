$( document ).ready(function() {
  $.ajaxPrefilter(function (options, originalOptions, jqXHR) {
    jqXHR.setRequestHeader('X-CSRF-Token', Cookies.get('csrftoken'));
  });

  $(document).ajaxStart(function () { 
    $("html").addClass("wait"); 
  });
  $(document).ajaxStop(function () { 
    $("html").removeClass("wait"); 
  });

  //$("#word_speaker").hide();
  $('body').on('click', "#button_next, #button_start",function(event){
  $("#button_next, #button_start").prop('disabled',true);
  $("html").addClass("wait");
  window.location.href = url_continue ;});
  //select meanings and words

  $("#interactbutton").prop('disabled',true);

  $('#meaning_inner .meaning_img').click(function(event){
    $("#word_speaker").show();

    if (! $('html').hasClass('wait')) {
      if(! $(this).hasClass('selected_m')) {
        $(".selected_m").removeClass("selected_m");
        $(this).addClass("selected_m");

        if ($(".selected_w").length > 0) {
          $("#interactbutton.interact_speaker").prop('disabled',false);
        };
        $("#interactbutton.interact_hearer").prop('disabled',false);
      } else {
        $(this).removeClass("selected_m");
        $("#interactbutton").prop('disabled',true);
      };
    }
  });

  $('#word_inner .word_text_speaker').click(function(event){
    if (! $('html').hasClass('wait')) {
      if (! $(this).hasClass('selected_w')) {
        $(".selected_w").removeClass("selected_w");
        $(this).addClass('selected_w');
        if ($(".selected_m").length > 0) {
          $("#interactbutton").prop('disabled',false);
        };
      } else {
        $(this).removeClass("selected_w");
        $("#interactbutton").prop('disabled',true);
      };
    }
  });

  //interact button with ajax
  $("#interactbutton.interact_hearer").click(function(event){
    $("#interactbutton").prop('disabled',true);
    $.ajax({
      url: url_results_hearer_base + $(".selected_m").attr("meaning_name") + "/results_json/",
      success: function (result) {
        var result_json = JSON.parse(result);
        $.ajax({
          url: url_results_inner_base  + result_json.bool_succ,
          success: function (result2) {
            $("#choose").html(result2);
            set_language();
          }
        });
      }
    });
    return false;
  });

  $("#interactbutton.interact_speaker").click( function (event) {
    $("#interactbutton").prop('disabled',true);
    $.ajax({
      url: url_results_speaker_base + $(".selected_m").attr("meaning_name") + "-" + $(".selected_w").attr("word_name") + "/results_json/",
      success: function (result) {
        var result_json = JSON.parse(result);
        $.ajax({
          url: url_results_inner_base  + result_json.bool_succ,
          success: function (result2) {
            $("#choose").html(result2);
            set_language();
          }
        });
      }
    });
    return false;
  });

  //buttons
  $("#homebutton").click(function(){
    $("html").addClass("wait");
    window.location.href=url_home;
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