$(document).ready(function() {
  $('a.myLinkModal').click( function(event){
    event.preventDefault();
      $('.overlay').fadeIn(297,	function(){
      	  $('.overlay')
      			.css('display', 'grid')
      			.animate({opacity: 1}, 0);
      		$('.myModal__close')
      			.css('display', 'block');

      		$('.main_back, .myLinkModal, .all_footer')
      			.css('display', 'none');
    	});
  	});

	$('a.myModal__close').click( function(){
    	$('.overlay').animate({opacity: 0}, 198, function(){
      		$('.overlay').fadeOut(297);
      		$(this).css('display', 'none');
    	});
  	});
});
