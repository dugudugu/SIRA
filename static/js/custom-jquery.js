// CountUp function for Happy Endings counter
$(document).ready(function() {
    $(".num").counterUp({delay:15, time:1000});
});


// Function Menu Burger
$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });
  
  // Dropdown-menu function for mobile 
  // Credits to: Serdar Akarca
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
// Credits to: HTML Online Article
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