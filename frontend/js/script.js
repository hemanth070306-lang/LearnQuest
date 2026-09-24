document.getElementById("registerForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const language = document.getElementById("language").value;

    const message = document.getElementById("message");

    try {

        const response = await fetch("https://learnquest-4wp2.onrender.com/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password,
                preferred_language: language
            })
        });

        const data = await response.json();

        message.textContent = data.message;

        if (response.ok) {
            message.style.color = "green";
            document.getElementById("registerForm").reset();
        } else {
            message.style.color = "red";
        }

    } catch (error) {

        message.textContent = "Cannot connect to LearnQuest server.";
        message.style.color = "red";

        console.error(error);
    }

});