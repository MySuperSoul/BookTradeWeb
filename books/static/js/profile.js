function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = Cookies.get('csrftoken');
console.log(csrftoken);
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#password_form").submit(function (e) {
    var form = $(this);
    console.log(form.attr('action'));

    $.ajax({
       type: "post",
       url: "/books/api/update_password/",
        async: true,
        data: form.serialize(),
        dataType: "json",
        success: function (data) {
            if(data.code === 1){
                alert(data.error);
            }else {
                alert('success');
            }
        }
    });
    e.preventDefault();
});