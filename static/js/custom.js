// Function Menu Burger
(function() {
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('#' + burger.dataset.target);
  burger.addEventListener('click', function() {
    burger.classList.toggle('is-active');
    nav.classList.toggle('is-active');
  });
})();

// LightBox function credits to Marcos Oliveira 
function openModal() {
  document.getElementById('myModal').style.display = "block";}

function closeModal() {
  document.getElementById('myModal').style.display = "none";}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("item-slide");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}



