const form = document.getElementById("login-form");
const API_URL = "http://127.0.0.1:8001";

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new URLSearchParams();
    formData.append("username", document.getElementById("login-email").value);
    formData.append("password", document.getElementById("login-password").value);

    const response = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData.toString()
    });

    const data = await response.json();

    console.log("LOGIN RESPONSE:", data);

    if (!response.ok) {
        alert(data.detail || "Login failed");
        return;
    }

    localStorage.setItem("token", data.access_token);

    window.location.href =
        data.role === "admin" ? "admindisplay.html" : "userdisplay.html";
});
// const form = document.getElementById('login-form');
// const API_URL = "http://127.0.0.1:8001";

// form.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const formData = new URLSearchParams();
//     formData.append("username", document.getElementById('login-email').value);
//     formData.append("password", document.getElementById('login-password').value);
//     const response = await fetch(`${API_URL}/auth/login`, {
//         method: "POST",
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: formData
//     });
    
//     const data = await response.json();

//     console.log(data);

//     if (!response.ok) {
//         alert("Invalid login credentials");
//         return;
//     }

//     localStorage.setItem('token', data.access_token);

//     if (data.role === "admin") {
//         window.location.href = "admindisplay.html";
//     } else {
//         window.location.href = "userdisplay.html";
//     }
// });