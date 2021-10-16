import emailjs from 'emailjs.com'

//Contact Message Functionality//

function SendEmail(e) {
    e.preventDefault();

    emailjs.sendForm('gmail', 'gGarden', //form.current
            e.target, 'user_jNykmAiHAI1nHZ4amoFHp')
        .then((result) => {
            console.log(result.text);
        }, (error) => {
            console.log(error.text);
        });
    e.target.reset()
};

window.addEventListener("scroll", function () {
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
});

function toggle() {
    var header = document.getElementById('header');
    header.classList.toggle('active');
}

function toggleForm() {
    var container = document.querySelector('.container');
    var section = document.querySelector('section');
    container.classList.toggle('active');
    section.classList.toggle('active');
}

$('.collapsible').collapsible();
$('.modal').modal();
$('.dropdown-trigger').dropdown();