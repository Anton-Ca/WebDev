document.addEventListener('DOMContentLoaded', function() {
    // Get the burger menu button
    var burgerMenu = document.querySelector('#burger-menu');

    // Get the dropdown
    var dropdown = document.querySelector('.dropdown');

    // Set the visibility of the dropdown to hidden
    dropdown.style.visibility = 'hidden';

    // Toggle the visibility of the dropdown when the burger menu button is clicked
    burgerMenu.addEventListener('click', function() {
        if (dropdown.style.visibility === 'hidden') {
            dropdown.style.visibility = 'visible';
        } else {
            dropdown.style.visibility = 'hidden';
        }
    });
});

// Copy paste from above for second button
document.addEventListener('DOMContentLoaded', function() {
    // Get the burger menu button
    var burgerMenu = document.querySelector('#small-burger');

    // Get the dropdown
    var dropdown = document.querySelector('.dropdown-small');

    // Set the visibility of the dropdown to hidden
    dropdown.style.visibility = 'hidden';

    // Toggle the visibility of the dropdown when the burger menu button is clicked
    burgerMenu.addEventListener('click', function() {
        if (dropdown.style.visibility === 'hidden') {
            dropdown.style.visibility = 'visible';
        } else {
            dropdown.style.visibility = 'hidden';
        }
    });
});
