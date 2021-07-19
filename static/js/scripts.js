window.addEventListener("scroll", function () {
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

function toggleForm() {
    var container = document.querySelector('.container');
    var section = document.querySelector('section');
    container.classList.toggle('active')
    section.classList.toggle('active')
}