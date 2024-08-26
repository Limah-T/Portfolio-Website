// main.js
document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('header nav ul'); // Adjust selector as needed

    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('showing');
    });
});
