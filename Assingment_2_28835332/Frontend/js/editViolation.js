const token = sessionStorage.getItem('token');
if (!token) {
    alert('Please log in to access this page.');
    window.location.href = "portal.html";
}
const role = sessionStorage.getItem('role');
if (role !== 'admin') {
    alert('Access denied. Admins only.');
    window.location.href = "userdisplay.html";
}

const API_URL = "http://127.0.0.1:8001";
const perameter = new URLSearchParams(window.location.search);
const violationID = perameter.get('id');

async function loadViolation() {
    const response = await fetch(`${API_URL}/violations/violation/${violationID}`);
    const violation = await response.json();

    document.getElementById('ViolationDateTime').value = violation.violationDateTime;
    document.getElementById('Distance').value = violation.distance;
    document.getElementById('Direction').value = violation.direction;
    document.getElementById('Landmark').value = violation.landmark;
    document.getElementById('Road').value = violation.road;
    document.getElementById('Details').value = violation.violationDetails;
    document.getElementById('PersonnelNumber').value = violation.personnelNumber;
}

loadViolation();

const form = document.getElementById('edit-violation-form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const updatedViolation = {
        violationDateTime: document.getElementById('ViolationDateTime').value,
        distance: document.getElementById('Distance').value,
        direction: document.getElementById('Direction').value,
        landmark: document.getElementById('Landmark').value,
        road: document.getElementById('Road').value,
        ViolationDetails: document.getElementById('Details').value,
        personnelNumber: document.getElementById('PersonnelNumber').value
        };
    const responce = await fetch(`${API_URL}/violations/violation/${violationID}/update`, {
    method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${sessionStorage.getItem('token')}`
        },
    body: JSON.stringify(updatedViolation)
});

    const result = await responce.json();
    if (responce.ok) {
        alert('Violation updated successfully');
    } else {
        alert('Failed to update violation: ' + (result.message || responce.statusText));
    }
    console.log(result);

    window.location.href = "admindisplay.html";
});
