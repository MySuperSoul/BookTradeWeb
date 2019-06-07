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

/** * @returns {string}*/
function GetSuccessMessage(message) {
    return "<div class=\"alert alert-success alert-dismissible fade show\">\n" +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\">&times;</button>\n"+
        message + "</div>";
}

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

$("#addlist_form").submit(function (evt) {
    var $form = $("#addlist_form");
    var formdata = new FormData($form[0]);
    console.log(formdata);
    $.ajax({
       type: "post",
       url: "/books/addlist/",
        async: true,
        data: formdata,
        cache: false,
        processData: false,
        contentType: false,
        dataType: "json",
        success: function (data) {
            if(data.code === 1){
                alert(data.error);
            }else {
                $("#message_field").html(GetSuccessMessage(data.success));
            }
        }
    });
    evt.preventDefault();
});

$("#ISBN_link_search_btn").click(function (evt) {
    var ISBN = $("#ISBN").val();
    var url = "/books/api/search_link_ISBN/" + ISBN + "/";
    $.ajax({
       type : "post",
       url : url,
        dataType : "json",
        success: function (data) {
            $("#link").val(data.link);
        }
    });
    evt.preventDefault();
});