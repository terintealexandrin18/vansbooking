// Run this code when the DOM content is fully loaded

document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".btn-edit");
    const deleteButtons = document.querySelectorAll(".btn-delete");
    

    // Edit booking functionality

    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            let bookingURL = button.getAttribute("data-booking-id");

            // Redirect to the edit page for the booking ID

            window.location.href = location.origin + bookingURL;
        });
    });

    // Delete booking functionality
    
    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            let bookingURL = button.getAttribute("data-booking-id");

            // Redirect to the delete page for the booking

            window.location.href = location.origin + bookingURL;
        });
    });
});