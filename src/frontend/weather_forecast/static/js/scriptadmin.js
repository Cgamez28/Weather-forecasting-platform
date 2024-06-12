fetch('http://localhost:8080/show_users')
    .then(response => response.json())
    .then(data => {
        const usersList = document.getElementById('users-list');
        data.forEach(user => {
            const userDiv = document.createElement('div');
            userDiv.classList.add('user');
            userDiv.innerHTML = `
                <p><span class="id">ID:</span> ${user.id}</p>
                <p><span class="username">Username:</span> ${user.username}</p>
                <p><span class="location">Location:</span> ${user.location}</p>
                <p><span class="notifications">Receive Notifications:</span> ${user.receive_notifications ? 'Yes' : 'No'}</p>
                <p><span class="measurement">Preference Unit Measurement:</span> ${user.preference_unit_measurement}</p>
            `;
            usersList.appendChild(userDiv);
        });
    })
    .catch(error => console.error('Error fetching users:', error));