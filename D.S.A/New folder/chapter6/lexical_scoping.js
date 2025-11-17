//lexical scoping;
function outerFunction() {
    let outerVariable = 'I am from outer function';


    function innerFunction() {
        let innerVariable = 'I am from inner function';
        console.log(outerVariable); // Accessing outer function variable
        console.log(innerVariable); // Accessing inner function variable
    }
    innerFunction();
    // console.log(innerVariable); // Error: innerVariable is not defined


}

outerFunction();
// console.log(outerVariable); // Error: outerVariable is not defined
// console.log(innerVariable); // Error: innerVariable is not defined
//lexical scoping with nested


function parent(){
    let ParentName = "I am from parent function";
    function child(){
        let childname = "I am from child function";
        console.log(ParentName)
        console.log(childname);
    }

    return child;
}

let childFunction = parent();
childFunction(); // invoking child function

//in lexical scoping inner function can access outer function variable but outer function cannot access inner function variable 