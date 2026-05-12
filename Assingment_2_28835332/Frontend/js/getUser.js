const user_id = sessionStorage.getItem("user_id");
async function getUser() {
    const API_URL = "http://127.0.0.1:8001"
    try {
        const list = document.getElementById("User-list")
        const response = await fetch(`${API_URL}/users/${user_id}`)
        const user = await response.json()
        list.innerHTML = `
            <li>Email: ${user.email}</li>
            <li>Forename: ${user.forename}</li>
            <li>Surname: ${user.surname}</li>
            <li>Drivers Licence: ${user.driversLicence}</li>
            <li>Date of Birth: ${user.dateOfBirth}</li>
            <li>Phone Number: ${user.phoneNumber}</li>
            <li>Address Line 1: ${user.addressLine1}</li>
            <li>Address Line 2: ${user.addressLine2}</li>
            <li>City: ${user.city}</li>
            <li>State: ${user.state}</li>
            <li>Zip Code: ${user.zipCode}</li>
            <li>VIN: ${user.VIN}</li>
        `
    } catch (error) {
        console.error("Error fetching user:", error)
    }
}