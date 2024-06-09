function toggleAdditionalContent() {
    var additionalContent = document.querySelector('.additional-content');
    additionalContent.style.display = (additionalContent.style.display === 'none' || additionalContent.style.display === '') ? 'block' : 'none';
    console.log("Opened or closed.")
}

document.getElementById("see-more-btn").addEventListener('click', toggleAdditionalContent);

// document.addEventListener("DOMContentLoaded", function() {
//     const pages = document.querySelectorAll('.page');
//     const navLinks = document.querySelectorAll('.nav a');

//     navLinks.forEach(link => {
//         link.addEventListener('click', function(event) {
//             event.preventDefault();
//             const target = this.getAttribute('href').substring(1);
//             pages.forEach(page => {
//                 if (page.id === target) {
//                     page.style.display = 'block';
//                 } else {
//                     page.style.display = 'none';
//                 }
//             });
//         });
//     });
// });