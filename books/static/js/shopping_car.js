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

$("input[name=check]").bind('click', function () {
    var checked_items = $("input[name=check]:checked");
    CalculateCheckedNumber(checked_items);
    GetAllPriceSum(checked_items);
});

function CalculateCheckedNumber(checked_items) {
    $("#checked-num").html(checked_items.length);
}

function GetAllPriceSum(checked_items) {
    var total_price = 0;
    checked_items.each(function (index) {
        var checked_item = $(this);
        var num = checked_item.data('num');
        var price = checked_item.data('price');
        total_price += Number(num) * Number(price);
    });
    $("#checked-price").html("¥ " + total_price.toString());
}