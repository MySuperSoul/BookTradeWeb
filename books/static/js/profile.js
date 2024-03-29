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
function GetErrorMessage(message) {
    return "<div class=\"alert alert-danger alert-dismissible fade show\">\n" +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\">&times;</button>\n"+
        message + "</div>";
}

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

$("#comment_submit_form").submit(function (evt) {
    var path_name = window.location.pathname;
    var url = window.location.href;
    var book_id = path_name.split('/')[3];
    
    var form = $(this);
    $.ajax({
        type : "post",
        url : "/books/api/submit_comment/" + book_id + "/",
        async : true,
        data : form.serialize(),
        dataType : "json",
        success : function (data) {
            if(data.code === 1){
                alert(data.error);
            }else{
                console.log('success');
                window.location.href = url;
            }
        }
    });
    evt.preventDefault();
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
                $('html,body').animate({ scrollTop: 0 }, 500);
                $("#message_field").html(GetSuccessMessage(data.data.message));
            }
        }
    });
    evt.preventDefault();
});

$("#ISBN_link_search_btn").click(function (evt) {
    var ISBN = $("#book_name").val();
    var url = "/books/api/search_link_ISBN/" + ISBN + "/";
    $.ajax({
       type : "post",
       url : url,
        dataType : "json",
        success: function (data) {
           if (data.code === 1)  $("#link").val(data.error);
           else {
               $("#link").val(data.link);
               $("#ISBN").val(data.ISBN);
               $("#book_desc").val(data.description);
               $("#origin_price").val(data.sell_price);
           }
        }
    });
    evt.preventDefault();
});

$("#add_shopping_btn").click(function () {
   var book_id = $("#book_id_hidden").val();
   var number = document.getElementById('buy_book_number').value;
   var address = $("#buy_address").val();
   var phone = $("#buy_phone").val();
   var user_id = $("#user_id_hidden").val();
   // alert(number);
   var url = "/books/api/add_to_shopping_car/";
   $.ajax({
       type : "post",
       url : url,
       async : true,
       dataType : "json",
       data : {
           book_id : book_id,
           user_id : user_id,
           number : number,
           address : address,
           phone : phone
       },
       success : function (Respon) {
           if (Respon.code === 0){
               $("#message-field").html(GetSuccessMessage(Respon.data.message));
               $("#shop_add_modal").modal('hide');
               window.location.reload();
           }else{
                $("#message-field").html(GetErrorMessage(Respon.error));
           }
       }
   })
});