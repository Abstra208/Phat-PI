document.addEventListener("DOMContentLoaded", function() {
    const iconUser = document.getElementById("icon-user");
    const UserDiv = document.getElementById("UserDiv");
    const iconsett = document.getElementById("icon-sett");
    const SettDiv = document.getElementById("SettDiv");

    if (iconUser) {
        iconUser.addEventListener("click", function(event){
            event.stopPropagation(); // Prevents the event from bubbling up to the document
            SettDiv.style.visibility = "hidden";
            if (UserDiv.style.visibility !== "visible") {
                UserDiv.style.visibility = "visible";
            } else {
                UserDiv.style.visibility = "hidden";
            }
        });
    }

    // Prevent UserDiv from hiding when it's clicked
    if (UserDiv) {
        UserDiv.addEventListener("click", function(event){
            event.stopPropagation(); // Prevents the event from bubbling up to the document
        });
    }

    // Add an event listener to the document
    document.addEventListener("click", function(){
        if (UserDiv.style.visibility === "visible") {
            UserDiv.style.visibility = "hidden";
        }
    });


    if (iconsett) {
        iconsett.addEventListener("click", function(event){
            event.stopPropagation(); // Prevents the event from bubbling up to the document
            UserDiv.style.visibility = "hidden";
            if (SettDiv.style.visibility !== "visible") {
                SettDiv.style.visibility = "visible";
            } else {
                SettDiv.style.visibility = "hidden";
            }
        });
    }

    // Prevent UserDiv from hiding when it's clicked
    if (SettDiv) {
        SettDiv.addEventListener("click", function(event){
            event.stopPropagation(); // Prevents the event from bubbling up to the document
        });
    }

    // Add an event listener to the document
    document.addEventListener("click", function(){
        if (SettDiv.style.visibility === "visible") {
            SettDiv.style.visibility = "hidden";
        }
    });
});