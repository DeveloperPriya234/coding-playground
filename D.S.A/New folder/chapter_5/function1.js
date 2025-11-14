// function decleration
// function refrence
// function call

// function sayHello() {
//     console.log("Hello World");
// }

// sayHello();



// 


//parameters(a,b);function declaration
//arguments(5,10);function calling


// function addTwoNumbers(a, b) {
// console.log(a + b);
// }
// addTwoNumbers(5, 10);


/**
 * The function named multiply takes two parameters, multiplies them together, and logs the result to
 * the console.
 * @param a - 5
 * @param b - 10
 */
// function multiply(a,b){
// console.log(a*b);
// }
// multiply(5,10);

function add(num1,num2){
    return num1+num2;
}


let result =add(5,10);
console.log(result);


//anonymous function// function name is not defined

// function(username){
//     return "hello"+"username"
// }

// const getuser=function (username){
//     return "hello"+username
// }
// console.log(getuser("ajay"));




// const name =function(username = "priyaa")// default parameter{{
//     {return "hello "+username
// }
// console.log(name());


// 


//arrow function

const consolefruit=()=>{
    console.log("🍐")
}


consolefruit();


const getfruit = ()=>console.log("🍎");
getfruit();

const consolefruitname= fruit=>console.log(fruit);

consolefruitname("🍊");


//immediate invoked function expression(IIFE)

(function(){
    console.log("hello o a,iife");
})();

