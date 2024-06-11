document.addEventListener("DOMContentLoaded", function() {
    const dateCells = document.querySelectorAll(".date");

    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    const today = new Date();

    dateCells.forEach((cell, index) => {
        const futureDate = new Date(today);
        futureDate.setDate(today.getDate() + index);

        const day = days[futureDate.getDay()];
        const date = futureDate.getDate();
        const month = months[futureDate.getMonth()];

        cell.innerHTML = `${day}<br>${date} ${month}`;
        cell.setAttribute("data-date", futureDate.toISOString().split('T')[0]);  // Añadir atributo de data con la fecha
    });
});
