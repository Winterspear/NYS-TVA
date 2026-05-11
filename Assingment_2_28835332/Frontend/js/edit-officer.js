const token = localStorage.getItem("token");
const role = localStorage.getItem("role");
const API_URL = "http://127.0.0.1:8001"
const params = new URLSearchParams(window.location.search);
const personnelNumber = params.get("personnelNumber");
if (!token || role !== "admin") {
    window.location.href = "portal.html";
}
async function loadOfficer() {
    const response = await fetch(`${API_URL}/officers/${personnelNumber}`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    const officer = await response.json();
    document.getElementById("firstname").value = officer.firstname;
    document.getElementById("lastname").value = officer.lastname;
    document.getElementById("department").value = officer.department;
    document.getElementById("detatchment").value = officer.detatchment;
}
loadOfficer();
const form = document.getElementById("edit-form");
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const updatedOfficer = {
        firstname: document.getElementById("firstname").value,
        lastname: document.getElementById("lastname").value,
        detatchment: document.getElementById("detatchment").value,
        department: document.getElementById("department").value
    };
    const response = await fetch(
        `${API_URL}/officers/${personnelNumber}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(updatedOfficer)
        }
    )
    if (response.ok) {
        alert("Officer updated successfully");
        window.location.href = "admin-officers.html";
    } else {
        alert("Failed to update officer");
    }
});
