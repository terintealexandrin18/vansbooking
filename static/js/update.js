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
    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            let bookingURL = button.getAttribute("data-booking-id");
            window.location.href = location.origin + bookingURL;
        });
    });
});