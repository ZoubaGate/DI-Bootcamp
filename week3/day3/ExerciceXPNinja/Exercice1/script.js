let add = document.getElementById("add-box");
add.addEventListener("click",func);

function func(e){
    let carre = document.createElement("div");
    carre.setAttribute('class','box');
    add.appendChild(carre);

}