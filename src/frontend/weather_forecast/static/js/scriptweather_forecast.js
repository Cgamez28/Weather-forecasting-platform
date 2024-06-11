document.addEventListener("DOMContentLoaded", function() {
    const dateCells = document.querySelectorAll(".date");

    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    
    // Get tomorrow's date
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1); // Add 1 day to get tomorrow
    
    dateCells.forEach((cell, index) => {
      const futureDate = new Date(tomorrow);
      futureDate.setDate(tomorrow.getDate() + index); // Set date for each cell relative to tomorrow
    
      const day = days[futureDate.getDay()];
      const date = futureDate.getDate();
      const month = months[futureDate.getMonth()];
    
      cell.innerHTML = `${day}<br>${date} ${month}`;
      cell.setAttribute("data-date", futureDate.toISOString().split('T')[0]);
    });
    
    const forecastForm = document.getElementById("forecastForm");
    const forecastLocation = document.getElementById("forecastLocation");
    const forecastUnit = document.getElementById("forecastUnit");

    async function getWeatherData(location, datetime) {
        const response = await fetch(`http://localhost:8080/get_forecast_data?time=${encodeURIComponent(datetime)}&location=${encodeURIComponent(location)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'http://localhost:8000',
                "Access-Control-Allow-Methods": "GET"
            },
        });

        if (response.ok) {
            return await response.json();
        } else {
            console.error("Error fetching weather data", await response.text());
            return null;
        }
    }
    
    async function updateWeatherForecast(location, unit) {
        const times = ["00:00:00", "03:00:00", "06:00:00", "09:00:00", "12:00:00", "15:00:00", "18:00:00", "21:00:00"];
        const forecastRows = document.querySelectorAll(".time");

        for (let i = 0; i < forecastRows.length; i++) {
            const row = forecastRows[i];
            const time = times[i];

            for (let j = 1; j <= 5; j++) {
                const dateCell = dateCells[j - 1];
                const date = dateCell.getAttribute("data-date");
                const datetime = `${date} ${time}`;

                const weatherData = await getWeatherData(location, datetime);

                if (weatherData) {
                    const temp = convertTemperature(weatherData.temperature, unit);
                    const tempUnit = getTemperatureUnit(unit);
                    const icon = getWeatherIcon(weatherData.weather_condition);

                    const cell = row.cells[j];
                    cell.innerHTML = `<img src="{% static '../static/images/${icon}' %}" alt="${weatherData.weather_condition}"><br>${temp}°${tempUnit}`;
                }
            }
        }
    }

    function getWeatherIcon(condition) {
        if (condition.toLowerCase().includes("clouds")) {
            return "cloudy-day-2.svg";
        } else if (condition.toLowerCase().includes("rain")) {
            return "rainy.svg";
        } else {
            return "day.svg";
        }
    }

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

    forecastForm.addEventListener('submit', async function(event) {
        event.preventDefault();  // Prevenir el envío del formulario
        const location = forecastLocation.value;
        const unit = forecastUnit.value;
        updateWeatherForecast(location, unit);
    });

});