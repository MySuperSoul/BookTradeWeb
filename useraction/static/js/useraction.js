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

function CheckEmail(email) {
    var reg = /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/;
    return reg.test(email);
}

/** * @returns {string}*/
function GetMessage(message) {
    return "<div class=\"alert alert-danger alert-dismissible\">\n" +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\">&times;</button>\n"+
        message + "</div>";
}

/** * @returns {string}*/
function GetSuccessMessage(message) {
    return "<div class=\"alert alert-success alert-dismissible\">\n" +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\">&times;</button>\n"+
        message + "</div>";
}

/** * @returns {boolean} */
function CheckEmpty(username, email, password) {
    if (username === "" || email === "" || password === "") return false;
    else return true;
}

function Register() {
    var username = $("#username").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var second_password = $("#second_password").val();

    if(CheckEmpty(username, email, password) === false){
        $("#message-field").html(GetMessage("用户名/邮箱/密码不能为空"));
        return;
    }

    if (CheckEmail(email) === false){
        $("#message-field").html(GetMessage("邮箱不符合格式"));
        return;
    }

    if(password !== second_password){
        $("#message-field").html(GetMessage("两次密码输入不一致"));
        return;
    }

    $.ajax({
        type : "post",
        url : "/auth/register/",
        async : true,
        data : {
            username : username,
            email : email,
            password : password,
        },
        dataType : "json",
        success : function (data) {
            if (data.code === 1)
                $("#message-field").html(GetMessage(data.error));
            else
                $("#message-field").html(GetSuccessMessage(data.data));
        }
    })
}