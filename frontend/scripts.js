
document.addEventListener('DOMContentLoaded', () => {
    // Selecciona los botones y el menú lateral
    const hamburger = document.querySelector('.hamburger');
    const closeBtn = document.querySelector('.close-btn');
    const sideMenu = document.querySelector('.side-menu');

    // Cuando se haga clic en la hamburguesa, abrir el menú lateral
    hamburger.addEventListener('click', () => {
      sideMenu.classList.add('open');
    });

    // Cuando se haga clic en la cruz, cerrar el menú lateral
    closeBtn.addEventListener('click', () => {
      sideMenu.classList.remove('open');
    });
});
