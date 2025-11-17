//*outside of the function or block
//! anything we add in var whose value add in window object
// var a =10; // global scope(anywhere i can access it)

// function add(){
//     let a = 10
//     let b = 20

// }

// {
//     var name = "priya"
// }

let a = 10;
{
    console.log(a);
}

if(10>9){
    console.log(a);
}


//local scope
function add(){
    let a = 10
    let b = 20
    console.log(a+b);
}
add();
// console.log(a+b); // error

{
    let name = "priya"
    console.log(name);
}
// console.log(name); // error`


