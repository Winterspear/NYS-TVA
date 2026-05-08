const API_URL = "http://127.0.0.1:8000"
async function violationCardCreate() {
    try {
        const responce = await fetch(`${API_URL}/violations/allViolations`);
        const violations = await responce.json();
        const container = document.getElementById('violation-cards-container');
        container.innerHTML = ''; // Clear existing cards

        violations.forEach(violation => {
            const card = document.createElement('div');

            card.classList.add('violation-card');

            card.onclick = () => {
                window.location.href = `edit.html?id=${violation.violationID}`;
            }

            card.innerHTML = `
            <h3>Violation ID: ${violation.violationID}</h3>
            <p>Date and Time: ${violation.violationDateTime}</p>
            <p>Distance: ${violation.distance}</p>
            <p>Direction: ${violation.direction}</p>
            <p>Landmark: ${violation.landMark}</p>
            <p>Road: ${violation.road}</p>
            <p>Details: ${violation.details}</p>
            <p>Personnel Number: ${violation.personnelNumber}</p>
            `;

            container.appendChild(card);
        });
    } catch (error) {
        console.error('Error creating violation card:', error);
    }
};

violationCardCreate