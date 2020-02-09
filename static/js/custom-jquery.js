// CountUp function for Happy Endings counter
$(function() {
    $(".num").counterUp({delay:15, time:1000});
});
  
// Dropdown-menu function        
$(function() {
        $(".navbar-item.has-dropdown").click(function(e) {
            if ($(".navbar-burger").is(':visible')) {
                $(this).toggleClass("is-active");
            }
        });
        $(".navbar-item > .navbar-link").click(function(e) {
            if ($(".navbar-burger").is(':visible')) {
                e.preventDefault();
            }
        });
        $(window).resize(function(e) {
            if (!$(".navbar-burger").is(':visible') && $(".navbar-item.has-dropdown.is-active").length) {
                $(".navbar-item.has-dropdown.is-active").removeClass('is-active');
            }
        });
});

// Back to top of page
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 100) {
        $('#back2Top').fadeIn();
    } else {
        $('#back2Top').fadeOut();
    }
});
$(document).ready(function() {
    $("#back2Top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

});