async function loadDashboard() {

    try {

        const response = await fetch("https://learnquest-4wp2.onrender.com/dashboard", {
            method: "GET",
            credentials: "include"
        });

        const data = await response.json();

        if (!response.ok) {

            alert(data.message);
            window.location.href = "login.html";
            return;

        }

        const user = data.user;

        document.getElementById("studentName").textContent = user.name;
        document.getElementById("xp").textContent = user.xp;
        document.getElementById("coins").textContent = user.coins;
        document.getElementById("streak").textContent = user.streak;

        console.log("Dashboard data:", user);

    } catch (error) {

        console.error("Dashboard error:", error);

        alert("Cannot connect to LearnQuest server.");

    }
}


loadDashboard();
