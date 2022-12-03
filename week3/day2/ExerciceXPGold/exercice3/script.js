let root = document.getElementById("root");
let shoppingList=[];

//buy
let buy = document.getElementById("buy");
let ul = document.createElement("ul");
buy.appendChild(ul);
//form
let form = document.createElement("form");
let br = document.createElement("br");
//input
let input = document.createElement("input");

//button
let button = document.createElement("button");
button.innerHTML = "AddItem";

form.appendChild(input);
form.appendChild(button);
form.appendChild(br);



root.appendChild(form);

button.addEventListener("click",func);
function func(e){
    shoppingList.push(input.value);
    e.preventDefault();
}

//afficher
let afficher = document.createElement("button");
afficher.innerHTML = "Afficher";
form.appendChild(afficher);
form.appendChild(br);
form.addEventListener("click",affiche);
function affiche(e){
    for(let i of shoppingList){
        let li = document.createElement("li");
        li.textContent=i;
        ul.appendChild(li);
    }
    e.preventDefault();
}

//supprimer
let supprimer = document.createElement("button");

supprimer.innerHTML="supprimer";
form.appendChild(supprimer);
form.appendChild(br);
form.addEventListener("click",sup);
function sup(e){
    shoppingList=[];
}

