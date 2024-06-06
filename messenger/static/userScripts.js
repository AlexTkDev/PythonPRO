function checkUserStatus(username) {
    fetch(`/status/${username}/`)
        .then(response => response.json())
        .then(data => {
            const statusElements = document.querySelectorAll(`[data-username='${username}']`);
            statusElements.forEach(statusElement => {
                if (data.is_online) {
                    statusElement.innerText = "Online";
                    statusElement.classList.add("btn-success");
                    statusElement.classList.remove("btn-secondary");
                } else {
                    statusElement.innerText = "Offline";
                    statusElement.classList.add("btn-secondary");
                    statusElement.classList.remove("btn-success");
                }
            });
        })
        .catch(error => console.error('Error:', error));
}

function updateStatuses() {
    const userElements = document.querySelectorAll('[data-username]');
    const usernames = [...new Set(Array.from(userElements).map(element => element.getAttribute('data-username')))];
    usernames.forEach(username => {
        checkUserStatus(username);
    });
}

// Update statuses every 30 seconds
setInterval(updateStatuses, 30000);

// Initial update
document.addEventListener("DOMContentLoaded", updateStatuses);
