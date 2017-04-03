function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$(document).ready(function() {

    // CSRF Protectction for ajax

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.modal').modal();
    $('#subscribe-button').click(function() {
        $('#modal1').modal('open')
    })
    
    var frm = $('#form')
    var submit_button = $('#submit-form-button')
    var close_button = document.getElementById('close_button')
    submit_button.click(function() {
        console.log("clicked")
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function(response) {
                console.log("success");
                $('#form').html(response)
                console.log(response)
                $('#modal1').removeClass('modal-fixed-footer')
                submit_button.remove();
                close_button.href = ""
            },
            error: function(response) {
                $('#modal1').modal('open');
                $('#form').html(response.responseText);


            }

        })
    });
});
