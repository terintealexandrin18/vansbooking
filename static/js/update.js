// Run this code when the DOM content is fully loaded


document.addEventListener("DOMContentLoaded", function() {
    var editButtons = document.querySelectorAll(".btn-edit");
    var deleteButtons = document.querySelectorAll(".btn-delete");
    

    // Edit booking functionality

    editButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var bookingURL = button.getAttribute("data-booking-id");

            // Redirect to the edit page for the booking ID

            window.location.href = location.origin + bookingURL;
        });
    });

    // Delete booking functionality
    
    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var bookingURL = button.getAttribute("data-booking-id");

            // Redirect to the delete page for the booking

            window.location.href = location.origin + bookingURL;
        });
    });
});