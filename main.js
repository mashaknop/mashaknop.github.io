const reveals = document.querySelectorAll('.js-reveal');
const observer = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger grid items
      const delay = entry.target.closest('.grid') ? (Array.from(entry.target.parentElement.children).indexOf(entry.target)) * 120 : 0;
      setTimeout(() => entry.target.classList.add('visible'), delay);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

reveals.forEach(el => observer.observe(el));
