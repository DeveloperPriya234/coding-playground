// Write a function that returns the sum of two numbers.
function add(a,b){
    return a+b;
}
sum = add(3,5);
console.log("Sum of two numbers is: " + sum);


// Write a function that checks if a number is even or odd.


function isEvenOrOdd(num){
    if(num %2==0)
        return "Even";
    else
        return "Odd";
}
isEvenOrOddResult = isEvenOrOdd(7);
console.log("The number is: " + isEvenOrOddResult);




// Write a function that takes a name and returns "Hello, <name>!".
function greet(name){
    return "Hello, " + name + "!";
}
greeting = greet("Alice");
console.log(greeting);
// Write a function that returns the square of a number.
function square_num(num){
    return num ** 2;
}
squared = square_num(76);    
console.log("Square of the number is: " + squared);

// Write a function that converts Celsius to Fahrenheit.

function celsiusToFahrenheit(celsius){
    return (celsius * 9/5) + 32;

}
fahrenheit = celsiusToFahrenheit(25);
console.log("Fahrenheit value is: " + fahrenheit);


//Write a function that takes a user object and returns "First Last".

function fullname(user){
    return firstName + " " +lastName;

}
firstName = "John";
lastName = "Doe";
full_name = fullname();
console.log("Full name is: " + full_name);


function fullname(user){
    return user.firstName + " " + user.lastName;
}
user = {firstName: "John", lastName: "Doe"};
full_name = fullname(user);
console.log("Full name is: " + full_name);