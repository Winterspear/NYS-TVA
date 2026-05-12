const API_URL = "http://127.0.0.1:8001"
async function violationCardCreate() {
    try {
        const token = sessionStorage.getItem("token");
        const responce = await fetch(`${API_URL}/violations/allViolations`, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
        const violations = await responce.json();
        const container = document.getElementById('card-container');
        container.innerHTML = ''; // Clear existing cards

        violations.forEach(violation => {
            const card = document.createElement('div');

            card.classList.add('card');

            card.onclick = () => {
                window.location.href = `editViolation.html?id=${violation.violationID}`;
            }

            card.innerHTML = `
            <h3>Violation ID: ${violation.violationID}</h3>
            <p>Date and Time: ${violation.violationDateTime}</p>
            <p>Distance: ${violation.distance}</p>
            <p>Direction: ${violation.direction}</p>
            <p>Landmark: ${violation.landmark}</p>
            <p>Road: ${violation.road}</p>
            <p>Details: ${violation.violationDetails}</p>
            <p>Personnel Number: ${violation.personnelNumber}</p>
            `;

            container.appendChild(card);
        });
    } catch (error) {
        console.error('Error creating violation card:', error);
    }
};

violationCardCreate()