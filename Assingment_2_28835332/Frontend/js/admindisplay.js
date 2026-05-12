const ViolationCButton = document.getElementById("Violation_counter");
const ViolationCParagraph = document.getElementById("vio_counter");
const OfficerCButton = document.getElementById("Officer_counter");
const OfficerCParagraph = document.getElementById("off_counter");
const API_URL = "http://127.0.0.1:8001"
    ViolationCButton.addEventListener("click", async () => {

        ViolationCParagraph.textContent =
            "Loading Number of Violations...";

        try {

            const response = await fetch(
                `${API_URL}/violations/NumberOfViolations`
            );

            if (!response.ok) {
                throw new Error("Failed to fetch violations");
            }

            const count = await response.json();

            console.log("COUNT: ", count);

            ViolationCParagraph.textContent =
                `Number of Violations: ${count}`;

        } catch (error) {

            console.error(error);

            ViolationCParagraph.textContent =
                `Error: ${error.message}`;
        }
    });
if (OfficerCButton && OfficerCParagraph) {
    OfficerCButton.addEventListener("click", () => {
        let message;
        const API_URL = "http://127.0.0.1:8001"
        async function loadOfficers() {
            try {
                const responce = await fetch(`${API_URL}/officers/NumberOfOfficers`);
                if (!responce.ok) {
                    throw new Error('Failed to fetch officers');
                }
                const count = await responce.json()
                OfficerCParagraph.textContent = `Number of Officers: ${count}`;
            } catch (error) {
                console.error(error);

                OfficerCParagraph.textContent =
                `Error: ${error.message}`;
            }
        }
        loadOfficers();
     });
}