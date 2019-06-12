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

function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] === variable){return pair[1];}
       }
       return(false);
}

function GetUrl(page){
    current_url = window.location.href;
    if(getQueryVariable("sort") === false){
        current_url += "?page=" + page.toString();
    }else {
        current_url += "&page=" + page.toString();
    }
    window.location.href = current_url
}

$("#sorting-select").change(function (e) {
    var current_url = window.location.pathname;
    var sort = $(this).children('option:selected').val();
    window.location.href = current_url + '?sort=' + sort;
});