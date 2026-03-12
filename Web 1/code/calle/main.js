/* LOAD NAVBAR */

fetch("navbar.html")
  .then((res) => res.text())
  .then((data) => {
    document.getElementById("navbar").innerHTML = data;

    initNavbar();
  });

/* LOAD FOOTER */

fetch("footer.html")
  .then((res) => res.text())
  .then((data) => {
    document.getElementById("footer").innerHTML = data;
  });

/* NAVBAR INTERACTION */

function initNavbar() {
  const idrBtn = document.getElementById("idrBtn");
  const cartBtn = document.getElementById("cartBtn");
  const userBtn = document.getElementById("userBtn");

  const idrCard = document.getElementById("idrCard");
  const cartCard = document.getElementById("cartCard");
  const userCard = document.getElementById("userCard");

  idrBtn.onclick = () => {
    toggle(idrCard);
  };

  cartBtn.onclick = () => {
    toggle(cartCard);
  };

  userBtn.onclick = () => {
    toggle(userCard);
  };

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
