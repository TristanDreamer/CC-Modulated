const toggle = document.getElementById("theme-toggle");

toggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
        toggle.textContent = "☀️";
    } else {
        toggle.textContent = "🌙";
    }
});

document.getElementById("cta-btn").addEventListener("click", () => {
    alert("Thanks for visiting!");
});