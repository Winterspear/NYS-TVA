const ViolationCButton = document.getElementById("Violation_counter");
const ViolationCParagraph = document.getElementById("Vio_counter");
const OfficerCButton = document.getElementById("Officer_counter");
const OfficerCParagraph = document.getElementById("Off_counter");
if (ViolationCButton && ViolationCParagraph) {
    ViolationCButton.addEventListener("click", () => {
        let message;
        const API_URL = "http://127.0.0.1:8000"
        async function loadViolations() {
            const list = document.getElementById('violations-list');
            list.innerHTML = '<p class="Loading">Loading Number of Violations... </p>';
            try {
                const responce = await fetch(`${API_URL}/violations/NumberOfViolations`);
                if (!responce.ok) {
                    throw new Error('Failed to fetch violations');
                }
                const violations = await responce.json();
                if (violations.length === 0) {
                    list.innerHTML = '<p class="NoViolations">No violations found.</p>';
                    return;
                }
                ViolationParagraph.textContent = `Number of Violations: ${violations}`;
            } catch (error) {
                list.innerHTML = `<p class="Error">Error: ${error.message}</p>`;
            }
        }
        loadViolations();
     });
}
if (OfficerCButton && OfficerCParagraph) {
    OfficerCButton.addEventListener("click", () => {
        let message;
        const API_URL = "http://127.0.0.1:8000"
        async function loadOfficers() {
            const list = document.getElementById('officers-list');
            list.innerHTML = '<p class="Loading">Loading Number of Officers... </p>';
            try {
                const responce = await fetch(`${API_URL}/officers/NumberOfOfficers`);
                if (!responce.ok) {
                    throw new Error('Failed to fetch officers');
                }
                const officers = await responce.json();
                if (officers.length === 0) {
                    list.innerHTML = '<p class="NoOfficers">No officers found.</p>';
                    return;
                }
                OfficerCParagraph.textContent = `Number of Officers: ${officers}`;
            } catch (error) {
                list.innerHTML = `<p class="Error">Error: ${error.message}</p>`;
            }
        }
        loadOfficers();
     });
}