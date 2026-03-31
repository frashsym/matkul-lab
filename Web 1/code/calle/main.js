document.addEventListener("DOMContentLoaded", function () {
  console.log("JS jalan bro ✅");

  /* LOAD NAVBAR */
  fetch("navbar.html")
    .then((res) => {
      if (!res.ok) throw new Error("Navbar tidak ditemukan");
      return res.text();
    })
    .then((data) => {
      document.getElementById("navbar").innerHTML = data;
      initNavbar();
    })
    .catch((err) => console.error("Error navbar:", err));

  /* LOAD FOOTER */
  fetch("footer.html")
    .then((res) => {
      if (!res.ok) throw new Error("Footer tidak ditemukan");
      return res.text();
    })
    .then((data) => {
      document.getElementById("footer").innerHTML = data;
    })
    .catch((err) => console.error("Error footer:", err));
});

/* NAVBAR INTERACTION */
function initNavbar() {
  const idrBtn = document.getElementById("idrBtn");
  const cartBtn = document.getElementById("cartBtn");
  const userBtn = document.getElementById("userBtn");

  const idrCard = document.getElementById("idrCard");
  const cartCard = document.getElementById("cartCard");
  const userCard = document.getElementById("userCard");

  if (!idrBtn || !cartBtn || !userBtn) {
    console.warn("Element navbar belum kebaca semua");
    return;
  }

  idrBtn.onclick = () => toggle(idrCard);
  cartBtn.onclick = () => toggle(cartCard);
  userBtn.onclick = () => toggle(userCard);

  function toggle(card) {
    const cards = document.querySelectorAll(".dropdown");

    cards.forEach((c) => (c.style.display = "none"));

    if (card.style.display === "block") {
      card.style.display = "none";
    } else {
      card.style.display = "block";
    }
  }
}