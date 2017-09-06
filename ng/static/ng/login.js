$( document ).ready(function() {
    $.ajaxPrefilter(function (options, originalOptions, jqXHR) {
        jqXHR.setRequestHeader('X-CSRF-Token', Cookies.get('csrftoken'));
        });
    $(document).ajaxStart(function () { $("html").addClass("wait"); });
    $(document).ajaxStop(function () { $("html").removeClass("wait"); });

//uuid
function uuid()
{
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c === 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}


//user cookie

if (typeof Cookies.get('NamingGameUser') === 'undefined'){
    var user_str = uuid();
    Cookies.set('NamingGameUser',
        user_str
        );

    };

$.ajax({
                                    url: url_send_user_info+user_str,
                                    success: function(result2){
        
            window.location.href = url_home;}

    });
var user_str = Cookies.get('NamingGameUser');
 //window.location.href =  url_send_user_info+user_str;

$("#username").html(user_str);

    $(document).ajaxStop(function () { $("#username").html(user_str); });
});


