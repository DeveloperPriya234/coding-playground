// primitive
// 7 types : string, number , boolean,null,undefined,symbol,BigInt

// const score = 100
// const scoreValue = 100.3
// const isLoggedIn = false
// const outsideTemp = null
// let userEmail;
// console.log(typeof  score )
// console.log(typeof  scoreValue )
// console.log(typeof  isLoggedIn )
// console.log(typeof  outsideTemp )
// console.log(typeof  userEmail )

const id=Symbol('123')
const anotherId = Symbol('123')

console.log(id === anotherId);

const bigNumber =  34232432580227247299n
console.log(typeof bigNumber)

// Reference (non primitive)

// array,objects,functions

// aray is in square brackets
const heros =["shaktiman","naagraj","doga"]

console.log(typeof heros);

let myObj={
    name:'priya',
    age:19,
}


console.log(typeof myObj)



const myFunction = function(){
    console.log("hello world")
}

console.log(typeof myFunction)// function obj

//https://262.ecma-international.org/5.1/#sec-11.4.3


//+++++++++++++++++++++++++++++++
// two types of memory
// stack (primitive),heap(reference(non primitive))

let myYoutubename = "hiteshchoudharydotcom"

let anothername = myYoutubename
anothername = "chaiaurcode"
console.log(myYoutubename);
console.log(anothername)



let userOne = {
    email:"user@google.com",
    upi:"user@bl"
}

console.log



