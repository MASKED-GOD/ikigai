<script>
    document.getElementById('ikigaiForm').addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Collect the form data
        const formData = new FormData(this);

        // Send the data to the Flask backend
        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)), // Convert form data to JSON
            headers: {
                'Content-Type': 'application/json' // Set the content type to JSON
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok'); // Check for network response errors
            }
            return response.json(); // Parse the JSON from the response
        })
        .then(data => {
            // Display the predicted Ikigai result
            document.getElementById('result').innerHTML = `<h2>Your Ikigai: ${data.ikigai}</h2>`;
        })
        .catch(error => {
            console.error('Error:', error); // Log any errors to the console
            document.getElementById('result').innerHTML = `<h2>Sorry, something went wrong.</h2>`; // Show error message to the user
        });
    });
</script>
