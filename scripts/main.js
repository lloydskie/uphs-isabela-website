// Hamburger menu toggle and close on outside click
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
if (menuBtn && mobileMenu) {
  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    mobileMenu.classList.toggle('hidden');
    if (!mobileMenu.classList.contains('hidden')) {
      setTimeout(() => {
        document.addEventListener('click', closeMenuOnOutside);
      }, 0);
    } else {
      document.removeEventListener('click', closeMenuOnOutside);
    }
  });

  function closeMenuOnOutside(e) {
    if (!mobileMenu.contains(e.target) && e.target !== menuBtn) {
      mobileMenu.classList.add('hidden');
      document.removeEventListener('click', closeMenuOnOutside);
    }
  }
}
