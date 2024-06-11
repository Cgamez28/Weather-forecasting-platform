document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const unitSelect = document.getElementById('unit');

    searchForm.addEventListener('submit', async function(event) {
        event.preventDefault();  // Prevenir el envío del formulario

        const location = searchInput.value;
        const unit = unitSelect.value;

        try {
            // Realizar la solicitud de datos meteorológicos al backend
            const response = await fetch(`http://localhost:8080/get_weather_data?location=${encodeURIComponent(location)}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const weatherData = await response.json();
                updateWeatherInfo(weatherData, unit);
            } else {
                const errorData = await response.json();
                alert(errorData.detail || 'Failed to retrieve weather data. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
    function convertTemperature(kelvin, unit) {
        if (unit === 'Celsius') {
            return (kelvin - 273.15).toFixed(1);
        } else if (unit === 'Fahrenheit') {
            return ((kelvin - 273.15) * 9/5 + 32).toFixed(1);
        } else {
            return kelvin.toFixed(1);
        }
    }

    function getTemperatureUnit(unit) {
        if (unit === 'Celsius') {
            return 'C';
        } else if (unit === 'Fahrenheit') {
            return 'F';
        } else {
            return 'K';
        }
    }

    function updateWeatherInfo(data, unit) {
        const temperature = convertTemperature(data.temperature, unit);
        const feelsLike = convertTemperature(data.feels_like, unit);
        const temperatureUnit = getTemperatureUnit(unit);

        document.querySelector('.temperature').textContent = `${temperature}°${temperatureUnit}`;
        document.querySelector('.feels_like').textContent = `${feelsLike}°${temperatureUnit}`;
        document.querySelector('.weather_condition').textContent = data.weather_condition;
        document.querySelector('.wind_speed').textContent = `${data.wind_speed} m/s`;
        document.querySelector('.humidity').textContent = `${data.humidity}%`;

        // Actualizar la imagen basada en la condición climática
        const weatherIcon = document.querySelector('.temp-icon img');
        if (data.weather_condition.toLowerCase().includes('scattered')) {
            weatherIcon.src = "/static/images/day.svg";
        } else {
            weatherIcon.src = "/static/images/cloudy.svg";
        }

        // Actualizar la marca de tiempo
        const timestamp = new Date();
        document.getElementById('timestamp').textContent = `Last updated: ${timestamp.toLocaleTimeString()}`;
    }


});
