const token = localStorage.getItem("token");
const role = localStorage.getItem("role");
const API_URL = "http://127.0.0.1:8001"

if (!token || role !== "admin") {
    window.location.href = "portal.html";
}
async function loadOfficers() {
    const response = await fetch(`${API_URL}/officers`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    const officers = await response.json();

    const container = document.getElementById("officers-container");

    officers.forEach(officer => {
        const card = document.createElement("div");

        card.classList.add("card");
        card.innerHTML = `
        <h2>${officer.firstname} ${officer.lastname}</h2>
        <p>Personnel Number: ${officer.personnelNumber}</p>
        <p>Detatchment: ${officer.detatchment}</p>
        <p>Department: ${officer.department}</p>
        `;
        card.onclick = () => {
            window.location.href = `edit-officer.html?id=${officer.personnelNumber}`;
        };
        container.appendChild(card);
    });
}
loadOfficers();