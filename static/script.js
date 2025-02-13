document.addEventListener("DOMContentLoaded", function () {
    const noBtn = document.getElementById("no-btn");
    const noText = document.getElementById("no-text");

    if (noBtn) {
        const NO_RESPONSES = [
            "No 💔",
            "Pretty please? 🥺",
            "But we'd be so cute together! 💕",
            "One more chance, pookie?",
            "Don't break my heart :(",
            "What about a maybe?",
            "Please don't do this to me, I'm fragile",
        ];

        let noClicks = 0;

        noBtn.addEventListener("click", () => {
            noText.innerText = NO_RESPONSES[Math.min(noClicks, NO_RESPONSES.length - 1)];
            noClicks++;
        });
    }

    const generateBtn = document.getElementById("generate-btn");
    if (generateBtn) {
        generateBtn.addEventListener("click", async () => {
            const name = document.getElementById("name").value.trim();
            if (!name) {
                alert("Please enter a name!");
                return;
            }

            try {
                const response = await fetch("/generate_poem", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ name }),
                });

                const data = await response.json();
                document.getElementById("poem-text").innerText = data.poem || "Oops! No poem found. Try again.";
            } catch (error) {
                console.error(error);
                document.getElementById("poem-text").innerText = "Error generating poem. Please try again.";
            }
        });
    }
});