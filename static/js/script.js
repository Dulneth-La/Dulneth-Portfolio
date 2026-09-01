// Typing animation
const text = "Dulneth Lahiru";
const typingElement = document.getElementById("typing-name");

if (typingElement) {
    let index = 0;

    function typeText() {
        if (index < text.length) {
            typingElement.textContent += text.charAt(index);
            index++;
            setTimeout(typeText, 100);
        } else {
            setTimeout(eraseText, 3000);
        }
    }

    function eraseText() {
        if (index > 0) {
            typingElement.textContent = text.substring(0, index - 1);
            index--;
            setTimeout(eraseText, 50);
        } else {
            setTimeout(typeText, 500);
        }
    }

    typeText();
}

// Nav active state
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-links a');

navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
        link.classList.add('active');
    }
});

// Scroll reveal animation
const revealElements = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => revealObserver.observe(el));
