document.addEventListener("DOMContentLoaded", function() {
    const dateCells = document.querySelectorAll(".date");

    // Array of day and month names 
    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    // Get the current date
    const today = new Date();

    // Update the date cells
    dateCells.forEach((cell, index) => {
        const futureDate = new Date(today);
        futureDate.setDate(today.getDate() + index);

        const day = days[futureDate.getDay()];
        const date = futureDate.getDate();
        const month = months[futureDate.getMonth()];

        cell.innerHTML = `${day}<br>${date} ${month}`;
    });
});

