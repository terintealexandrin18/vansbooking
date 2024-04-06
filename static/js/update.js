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
            // Send an AJAX request to delete the booking
            
            let url = location.origin + bookingURL;
            console.log(url);
            console.log("URL : ")

            fetch(url, {
                method: 'GET'
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