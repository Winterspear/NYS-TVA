const role = sessionStorage.getItem("role");

if (role !== "admin") {

    window.location.href = "/portal.html";
}
document
    .getElementById("officer-button")
    .addEventListener("click", () => {

        window.location.href =
            "admin-officers.html";
    });

document
    .getElementById("violation-button")
    .addEventListener("click", () => {

        window.location.href =
            "admin-violations.html";
    });