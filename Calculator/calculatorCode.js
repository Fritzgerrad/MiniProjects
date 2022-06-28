var check = 0;
var firstNum = document.getElementById(firstNum).innerHTML;
var secNum = document.getElementById(secondNum).innerHTML;

function toAdd(){
check = 1;
}
function toSubtract(){
    check = 2;
}
function toDivide(){
    check  = 3;
}
function toMultiply(){
    check = 4;
}

function add(){
    return firstNum + secNum;
}
function subtract(){
    return firstNum - secNum;
}
function multiply(){
    return firstNum * secNum;
}
function divide(){
    return firstNum / secNum;
}

function solve(){
    if (check == 1){
        var result = add();
    }
    if (check == 2){
        var result = subtract();
    }
    if (check == 3){
        var result = divide();
    }
    if (check == 4){
        var result = multiply();
    }
    document.getElementById("result").innerHTML = result;
}