const form = document.getElementById('login-form');
const API_URL = "http://127.0.0.1:8001"
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new URLSearchParams();
    formData.append("email", document.getElementById('login-email').value);
    formData.append("password", document.getElementById('login-password').value);

    const responce = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData.toString()
    });
    if (!responce.ok) {
        alert("Invalid login credentials");
        return;
    }

    const data = await responce.json()

    localStorage.setItem('token', data.token);

    if (data.role === "admin") {
        window.location.href = "admindisplay.html";
    } else {
        window.location.href = "userdisplay.html";
    }
});
