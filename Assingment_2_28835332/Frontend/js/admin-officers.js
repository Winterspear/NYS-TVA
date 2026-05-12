const token = sessionStorage.getItem("token");
const role = sessionStorage.getItem("role");
const API_URL = "http://127.0.0.1:8001"

if (!token || role !== "admin") {
    window.location.href = "portal.html";
}
async function loadOfficers() {
    const response = await fetch(`${API_URL}/officers/AllOfficers`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    const officers = await response.json();
    console.log(officers)

    const container = document.getElementById("officer-container");

    officers.forEach(officer => {
        const card = document.createElement("div");

        card.classList.add("card");
        card.innerHTML = `
            <h2>${officer.firstName} ${officer.lastName}</h2>
            <p>Personnel Number: ${officer.personnelNumber}</p>
            <p>District: ${officer.district}</p>
            <p>Detachment: ${officer.detachment}</p>
        `;
        card.onclick = () => {
            window.location.href = `edit-officer.html?personnelNumber=${officer.personnelNumber}`;
        };
        container.appendChild(card);
    });
}
loadOfficers();