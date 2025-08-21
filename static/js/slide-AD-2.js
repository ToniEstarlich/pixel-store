
document.addEventListener('DOMContentLoaded', function() {
  const track = document.getElementById('advertsTrack');
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentIndex = 0;

  const animations = ['fadeInUp', 'zoomIn', 'fadeInLeft', 'fadeInRight'];

  // Duplicar primer slide al final para efecto loop
  const firstClone = slides[0].cloneNode(true);
  track.appendChild(firstClone);

  function animateText(index) {
    const text = track.children[index]?.querySelector('.adverts-text');
    if (text) {
      text.style.opacity = 0;
      text.style.animation = '';
      const anim = animations[Math.floor(Math.random() * animations.length)];
      setTimeout(() => {
        text.style.animation = `${anim} 1.5s ease forwards`;
      }, 200);
    }
  }

  function showSlide(index, instant = false) {
    const offset = -index * 100;
    if (instant) {
      track.style.transition = 'none';
    } else {
      track.style.transition = 'transform 1s ease-in-out';
    }
    track.style.transform = `translateX(${offset}%)`;
    if (!instant) animateText(index);
  }

  function nextSlide() {
    currentIndex++;
    showSlide(currentIndex);

    // Si llegamos al clone (último)
    if (currentIndex === totalSlides) {
      // Reset al primer slide instantáneamente después de la transición
      setTimeout(() => {
        currentIndex = 0;
        showSlide(currentIndex, true);
      }, 1000); // coincide con la duración de la transición
    }
  }

  // Inicial
  showSlide(currentIndex);

  // Auto-slide
  setInterval(nextSlide, 6000);
});
