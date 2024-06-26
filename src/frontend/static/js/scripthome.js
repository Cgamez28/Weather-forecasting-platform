let URL_BASE = "http://localhost:8080"

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginForm').addEventListener('submit', async function(event) {
        event.preventDefault(); 

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        let url_post = URL_BASE + '/login'

        try {
            const response = await fetch(url_post, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': 'http://localhost:8000',
                    "Access-Control-Allow-Methods": "POST"
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok) {
                window.location.href = 'http://127.0.0.1:8000/weather/current_weather/';  // Cambia '/welcome' a la ruta deseada
            } else {
                alert(data.detail || 'Login failed. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
});


