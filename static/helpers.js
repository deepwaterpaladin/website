function toggleAdditionalContent() {
    var additionalContent = document.querySelector('.additional-content');
    additionalContent.style.display = (additionalContent.style.display === 'none' || additionalContent.style.display === '') ? 'block' : 'none';
    console.log("Opened or closed.")
}

function toggleProjectsContent(){
    var projectsButton = document.querySelector('.projects-button');
    projectsButton.style.display = (projectsButton.style.display === 'none' || projectsButton.style.display === '') ? 'block' : 'none';
    console.log("Opened or closed.")
}

function getUsersLocation(){
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            
            console.log("Latitude: " + latitude + ", Longitude: " + longitude);
        }, function(error) {
            console.error("Error getting location:", error.message);
        });
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

document.getElementById("see-more-btn").addEventListener('click', toggleAdditionalContent);
document.getElementById("see-more-projects-btn").addEventListener('click', toggleProjectsContent);