$(document).ready(function(){
  $('.product_photos img').hover(function(){
  		var swap = $('.main_p').attr('src')
  		$('.main_p').attr('src', $(this).attr('src'));
  		$('.main_p').attr('alt', swap);
  	}, function(){
      var temp = $('.main_p').attr('alt')
      $('.main_p').attr('src', temp);
    });
})
