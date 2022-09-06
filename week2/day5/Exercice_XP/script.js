console.log("Bienvenue dans ce jeu de devinette !");
console.log("Votre objectif est de trouver un nombre ENTIER entre 1 et 10");
console.log("Pour se faire, vous n\'aurez droit qu\'à 3 essais");

function playTheGame(){
    var reponse=confirm("souhaitiez vous jouer a ce jeu? ");
    if(reponse==false){
        alert("Pas de problème, au revoir");
    }
    else{
        var userNumber=0;
        var computerNumber = Math.floor(Math.random() * 10)+1;
        alert(computerNumber);
        while(!Number(userNumber) || Number(userNumber)<0 || Number(userNumber)>10){
            userNumber = Number(prompt("userNumber un nombre compris entre 1 et 10: "));
        }
        compareNumbers(userNumber,computerNumber);
        
    }
}

function compareNumbers(userNumber,computerNumber){
    var chance = 3;
    for(chance=0;chance<3;chance++){
        if(userNumber>computerNumber){
            chance+=1;
            userNumber =prompt("Votre numéro est plus grand que celui de l'ordinateur,\n devinez à nouveau: ");
        }
        else if(userNumber<computerNumber){
            chance+=1;
            userNumber = prompt("Votre numéro est plus petit que celui de l'ordinateur, devinez à nouveau");
        }
        else if(userNumber==computerNumber){
            alert("WINNER");
            break;
        }
    }
    if (userNumber !== computerNumber) {
        alert("Dommage, tu n'as pas trouvé la réponse dans les 3 essais impartis. La réponse était " + computerNumber);
    }
}
