// CountUp function for Happy Endings counter
jQuery(document).ready(function($) {
            $(".num").counterUp({delay:15, time:1000});
        });

// jQuery function for form validator         
//$(function() {
    //$("form[name='registration']").validate({
    // Specify validation rules
   // rules: {
    //  name: "required",
     // email: {
    //    required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
     //   email: true
     // },
     // phone: "required",
     // subject: "required",
      //question: "required"
   // },
    // Specify validation error messages
   // messages: {
   //   name: "Please enter your name",
   //   email: "Please enter a valid email address",
   //   phone: "Please enter a valid phone nummber",
   //   subjet: "Please enter your subject for contacting us",
   //   question: "Please enter your question"
  //  },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
   // submitHandler: function(form) {
  //    form.submit();
  //  }
 // });
//});