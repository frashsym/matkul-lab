function loadComponent(id, file) {
    fetch(file)
        .then(response => response.text())
        .then(data => {
            document.getElementById(id).innerHTML = data;
        });
}
loadComponent("header", "header.html");
loadComponent("rinci_produk", "rinci_produk.html");
loadComponent("footer", "footer.html");
