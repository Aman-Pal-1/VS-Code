// Add smooth scroll animation to anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Hover effect for navigation links
const navLinks = document.querySelectorAll('nav ul li a');
navLinks.forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.color = '#d7b598'; // Lighter brown on hover
    });

    link.addEventListener('mouseout', () => {
        link.style.color = 'white'; // Default color
    });
});
