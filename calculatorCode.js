var check = 0;
var firstNum = document.getElementById(firstNum);
var secNum = document.getElementById(secondNum);

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
        add();
    }
    if (check == 2){
        subtract();
    }
    if (check == 3){
        divide();
    }
    if (check == 4){
        multiply();
    }
}