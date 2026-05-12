const token = sessionStorage.getItem("token");
const role = sessionStorage.getItem("role");
const API_URL = "http://127.0.0.1:8001"
const params = new URLSearchParams(window.location.search);
const personnelNumber = params.get("personnelNumber");
if (!token || role !== "admin") {
    window.location.href = "portal.html";
}
async function loadOfficer() {
    const response = await fetch(`${API_URL}/officers/find/${personnelNumber}`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    const officer = await response.json();
    console.log(officer);
    document.getElementById("firstname").value = officer.firstName;
    document.getElementById("lastname").value = officer.lastName;
    document.getElementById("district").value = officer.district;
    document.getElementById("detachment").value = officer.detachment;
}
loadOfficer();
const form = document.getElementById("edit-form");
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const updatedOfficer = {
        firstName: document.getElementById("firstname").value,
        lastName: document.getElementById("lastname").value,
        detachment: parseInt(document.getElementById("detachment").value),
        district: parseInt(document.getElementById("district").value)
    };
    const response = await fetch(
        `${API_URL}/officers/update/${personnelNumber}`,
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
