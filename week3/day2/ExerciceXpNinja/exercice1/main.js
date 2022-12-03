
let calculate = document.getElementById("calculate");
calculate.addEventListener("click",calculateTip);
function calculateTip(e){
    let billAmount = document.getElementById("billamt").value;
    let serviceQuality = document.getElementById("serviceQual").value;
    
    let numberOfPeople = document.getElementById("peopleamt").value;
    //  alert(serviceQuality);

    if(serviceQuality==0 || billAmount==0){
        alert("enter valeur");
    }
    
     if (numberOfPeople<1){
         numberOfPeople=1;
    }
    document.getElementById("each").innerHTML='';


    let total = ( billAmount * serviceQuality ) / numberOfPeople;
    total = total.toFixed(3);
    let totalTip = document.getElementById("totalTip");
    totalTip.style.display = "block";
    
    let tip = document.getElementById("tip");
    tip.textContent=total;
    e.preventDefault();

}