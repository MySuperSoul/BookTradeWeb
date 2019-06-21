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

function changeURLArg(url,arg,arg_val){
    var pattern=arg+'=([^&]*)';
    var replaceText=arg+'='+arg_val;
    if(url.match(pattern)){
        var tmp='/('+ arg+'=)([^&]*)/gi';
        tmp=url.replace(eval(tmp),replaceText);
        return tmp;
    }else{
        if(url.match('[\?]')){
            return url+'&'+replaceText;
        }else{
            return url+'?'+replaceText;
        }
    }
    return url+'\n'+arg+'\n'+arg_val;
}

function GetUrl(page){
    var current_url = window.location.href;
    var page_url = changeURLArg(current_url, 'page', page);
    window.location.href = page_url;
}

$("#sorting-select").change(function (e) {
    var current_url = window.location.pathname;
    var sort = $(this).children('option:selected').val();
    window.location.href = current_url + '?sort=' + sort;
});

$("#price-filter-btn").click(function (w) {
   var min_price = $("#price-control").val().split(',')[0];
   var max_price = $("#price-control").val().split(',')[1];
   current_url = window.location.href;
   if (current_url.indexOf("min") !== -1){
       var index = current_url.indexOf("min");
       var url = current_url.substring(0, Number(index) - 1);
       current_url = url;
   }

   if (current_url.indexOf('?') !== -1){
       current_url += ('&min=' + min_price + '&max=' + max_price);
   }else {
       current_url += ('?min=' + min_price + '&max=' + max_price);
   }
   window.location.href = current_url;
});