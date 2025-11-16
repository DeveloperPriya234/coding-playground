//scope 
//local scope(function scope
function test() {
    var a = 30;
    console.log(a); //30
}
test();
//console.log(a); //ReferenceError: a is not defined
//global scope
var b = 40;
console.log(b);






//block scope

if (true) {
    let c = 50;
    console.log(c); //50


}//console.log(c); //ReferenceError: c is not defined
for (let i = 0; i < 3; i++) {
    console.log(i); //0 1 2
}
//console.log(i); //ReferenceError: i is not defined
{
    const d = 60;
    console.log(d); //60
}


//console.log(d); //ReferenceError: d is not defined    
