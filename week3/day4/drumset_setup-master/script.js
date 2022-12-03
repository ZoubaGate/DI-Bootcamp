
var allowed_keys = [65,83,68,70,71,72,74,75,76];

window.addEventListener('keydown', function(e){
    var keyCode = e.keyCode;
    if(!allowed_keys.includes(keyCode)) return;
    e.preventDefault();
    e.stopPropagation();
    playAudio(keyCode);
})

var drums = document.getElementsByClassName("drum");
for(i of drums){
    i.addEventListener("click",function(e){
        var keyCode = this.getAttribute("data-key");
        playAudio(keyCode);
    })
}

function playAudio(keyCode){
    var note = document.querySelector("audio[data-key='"+keyCode+"']");
    var drum = document.querySelector(".drum[data-key='"+keyCode+"']");
    note.currentTime=0;
    drum.classList.add("playing");
    setTimeout(function(){
        drum.classList.remove("playing");
    },100)
    note.play();
}