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
    var total_price = GetAllPriceSum(checked_items);
    $("#checked-price").html("¥ " + total_price.toString());
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
    return total_price;
}

$("#shopping-car-btn").click(function () {
    var checked_items = $("input[name=check]:checked");
    var value_array = [];
    checked_items.each(function (index) {
        value_array.push($(this).val());
    });
    console.log(value_array);
    $.ajax({
        type : "post",
        url : "/books/shopping_car/",
        async : true,
        traditional : true,
        dataType : "json",
        data : {
            'values' : JSON.stringify(value_array),
            'type' : 'offer',
            'price' : GetAllPriceSum(checked_items)
        },
        success : function (data) {
            if (data.code === 0) alert(data.data.message);
            else alert(data.error);
            window.location.reload();
        }
    })
});

function DeleteView(id) {
    id = Number(id);
    $.ajax({
        type: "post",
        url: "/books/shopping_car/",
        async: true,
        dataType: "json",
        data: {
            'id': id,
            'type': 'delete'
        },
        success: function (data) {
            window.location.reload();
            alert(data.data.message);
        }
    });
}

function VerifyOrder(order_id) {
    order_id = Number(order_id);
    $.ajax({
        type: "post",
        url: "/books/api/verify_order/",
        async: true,
        dataType: "json",
        data: {
            order_id: order_id
        },
        success : function (data) {
           window.location.reload();
           alert(data.data.message);
        }
    })
}

$("#add_account_btn").click(function (e) {
       var add_number = $("#buy_number").val();
       if (add_number === ''){
           alert('充值金额不能为空');
       } else {
           $.ajax({
               type : "post",
               url : "/books/api/add_credit_account/",
               async : true,
               dataType : "json",
               data : {
                   'number' : Number(add_number)
               },
               success : function (data) {
                   var html = "<strong>当前余额为：</strong>" + data.data.number + " ¥";
                   $("#account-text").html(html);
                   $("#buy_number").val('充值成功');
               }
           })
       }
});