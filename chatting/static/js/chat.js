$(document).ready(function(){

	var msg_template = '<p><span class="msg-block"><strong></strong><span class="time"></span><span class="msg"></span></span></p>';

	$('.chat-message button').click(function(){
		var input = $(this).siblings('span').children('input[type=text]');
		if(input.val() !== ''){
			add_message('You','img/demo/av1.jpg',input.val(),true);
		}
	});

	$('.chat-message textarea').keypress(function(e){
		if(e.which === 13) {
			if($(this).val() !== ''){
				add_message('You','img/demo/av1.jpg',$(this).val(),true);
			}
		}
	});

   	var i = 0;
	function add_message(name,img,msg,clear) {
		i = i + 1;
		var  inner = $('#chat-messages-inner');
		var time = new Date();
		var hours = time.getHours();
		var minutes = time.getMinutes();
		if(hours < 10) hours = '0' + hours;
		if(minutes < 10) minutes = '0' + minutes;
		var id = 'msg-'+i;
        var idname = name.replace(' ','-').toLowerCase();
		inner.append('<p id="'+id+'" class="user-'+idname+'"><img src="'+img+'" alt="" />'
										+'<span class="msg-block"><strong>'+name+'</strong> <span class="time">- '+hours+':'+minutes+'</span>'
										+'<span class="msg">'+msg+'</span></span></p>');
		$('#'+id).hide().fadeIn(800);
		if(clear) {
			$('.chat-message textarea').val('').focus();
		}
		$('#chat-messages').animate({ scrollTop: inner.height() },1000);
	}
});
