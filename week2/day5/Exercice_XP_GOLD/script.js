function equal(){
    let var1 = document.getElementById("result").innerHTML; 
             						let var2 = eval(var1) ;
             						document.getElementById("result").innerHTML = var2;
}
function number(num){
    document.getElementById("result").innerHTML+=num;
}
function operator(operator){
    document.getElementById("result").innerHTML+=operator;
}
function reset(){
    document.getElementById("output").innerHTML="";
}
function clear(){
let len = document.getElementById("result").innerHTML;
    let len2=len.length;
    len=len.substring(0,len2-1);
    document.getElementById("result").innerHTML=len;

}
