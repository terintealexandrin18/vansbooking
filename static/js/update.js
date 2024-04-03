document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".btn-edit");
    const deleteButtons = document.querySelectorAll(".btn-delete");

    // Edit booking functionality
    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            let bookingId = button.getAttribute("data-booking-id");
            // Redirect to the edit page for the booking ID
            window.location.href = `/edit_booking/${bookingId}`;
        });
    });

    // Delete booking functionality
    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            let bookingId = button.getAttribute("data-booking-id");
            // Send an AJAX request to delete the booking
            fetch(`/delete_booking/${bookingId}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    // Reload the page after successful deletion
                    window.location.reload();
                } else {
                    console.error('Failed to delete booking');
                }
            })
            .catch(error => {
                console.error('Error deleting booking:', error);
            });
        });
    });
});