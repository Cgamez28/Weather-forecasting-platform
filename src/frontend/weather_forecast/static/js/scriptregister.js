document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('registerForm').addEventListener('submit', async function(event) {
        event.preventDefault(); 

        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const location = document.getElementById('location').value;
        const receive_notifications = document.getElementById('receive_notifications').value;
        const preference_unit_measurement = document.getElementById('preference_unit_measurement').value;

        try {
            const response = await fetch('http://localhost:8080/create_user', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    username, 
                    password, 
                    location, 
                    receive_notifications, 
                    preference_unit_measurement 
                }),
            });

            const data = await response.json();

            if (response.ok) {
                window.location.href = 'http://127.0.0.1:8000/weather/';  
            } else {
                alert(data.detail || 'Registration failed. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    })
});