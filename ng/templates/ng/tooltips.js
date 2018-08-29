{% load static %}
{% load i18n %}


    $('#home').tooltip({
      title : {% trans "Home" %} ,//current_lang.btn_home,
      placement : "right auto",
      trigger: "hover focus",
    });

    $('#groop_3').tooltip({
      title : {% trans "You are 3" %} ,//current_lang.groop_3,
      placement : "right auto",
      trigger: "hover focus",
    });

    $('#groop_5').tooltip({
      title : {% trans "You are 5" %} ,//current_lang.groop_5,
      placement : "right auto",
      trigger: "hover focus",
    });
