let valider = document.getElementById("button");
valider.addEventListener("click",validate);

function checkEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
function validate(e) {
    var email = document.getElementById("email").value;
    if (checkEmail(email)) {
        alert('Adresse e-mail valide');
    } else {
        alert('Adresse e-mail non valide');
    }
    return false;
    e.preventDefault();
}

