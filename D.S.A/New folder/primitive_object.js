//primitive
//there are 7 types of primitive  data types in javascript
//1. number
//2. string 
//3. boolean
//4. undefined
//5. null
//6. bigInt
//7. symbol
let a = 45; //number
let b = "harry"; //string
let c = true;   //boolean
let d = undefined; //undefined                      
let e = null; //null
let f = BigInt("567") + BigInt("3");
let g = Symbol
("i am a nice symbol");
console.log("type of a is ", typeof a);
console.log("type of b is ", typeof b);
console.log("type of c is ", typeof c);
console.log("type of d is ", typeof d);
console.log("type of e is ", typeof e); 
console.log("type of f is ", typeof f);
console.log("type of g is ", typeof g);
//non-primitive data types
//object
//array
//function
//object
//in javascript object is a collection of key value pairs
let obj = {
    harry: 90,
    shubham: 56,    
    rohan: 78,
    "my channel": 45,
}
console.log(obj);
console.log(typeof obj);

