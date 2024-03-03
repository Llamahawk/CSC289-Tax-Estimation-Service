var display = true;
var username = "User";

function loggedIn()
{
    if (display == true)
    {
        location.href = "main.html";
        document.getElementById("bannerButtons").innerHTML = username;
    }
}