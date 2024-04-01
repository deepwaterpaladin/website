function toggleAdditionalContent() {
    var additionalContent = document.querySelector('.additional-content');
    additionalContent.style.display = (additionalContent.style.display === 'none' || additionalContent.style.display === '') ? 'block' : 'none';
    console.log("Opened or closed.")
}
document.getElementById("see-more-btn").addEventListener('click', toggleAdditionalContent);
