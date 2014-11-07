$('.navbar .dropdown').hover(function() {
	if($(window).width() > 767){
		$(this).find('.dropdown-menu').first().stop(true, true).slideDown(150);
	}
}, function() {
	if($(window).width() > 767){
		$(this).find('.dropdown-menu').first().stop(true, true).slideUp(105)
	}
});