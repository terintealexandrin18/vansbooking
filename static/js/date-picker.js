// Custom JavaScript to restrict past dates

document.addEventListener('DOMContentLoaded', function() {
    var dateInput = document.querySelector("input[type='date']");
    if (dateInput) {
        var today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }
});