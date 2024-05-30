document.addEventListener("DOMContentLoaded", function() {
    const dateCells = document.querySelectorAll(".date");

    // Array de nombres de días y meses en español
    const days = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"];
    const months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];

    // Obtiene la fecha actual
    const today = new Date();

    //Actualiza las celdas de fecha
    dateCells.forEach((cell, index) => {
        const futureDate = new Date(today);
        futureDate.setDate(today.getDate() + index);

        const day = days[futureDate.getDay()];
        const date = futureDate.getDate();
        const month = months[futureDate.getMonth()];

        cell.innerHTML = `${day}<br>${date} ${month}`;
    });
});
