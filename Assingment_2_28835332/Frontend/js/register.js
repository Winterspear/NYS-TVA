const form = document.getElementById("register-form");
const API_URL = "http://127.0.0.1:8000"
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const password = document.getElementById("password").value;
    const confirm = document.getElementById("confirm").value;
    if (password !== confirm) {
        alert("Passwords do not match");
        return;
    }

    const formData = {
        forename: document.getElementById("forename").value,
        surname: document.getElementById("surname").value,
        email: document.getElementById("email").value,
        password: password,
        driversLicence: document.getElementById("licence").value,
        dateOfBirth: document.getElementById("dateofbirth").value,
        phoneNumber: document.getElementById("phone").value,
        addressLine1: document.getElementById("addressL1").value,
        addressLine2: document.getElementById("addressL2").value,
        city: document.getElementById("city").value,
        state: document.getElementById("state").value,
        zipCode: document.getElementById("zip").value,
        VIN: document.getElementById("vin").value
    }
    const response = await fetch(`${API_URL}/users/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });
    const data = await response.json();
    if (response.ok) {
        alert("Registration successful");
        window.location.href = "login.html";
    } else {
        alert(`Registration failed: ${data.message}`);
    }
    });