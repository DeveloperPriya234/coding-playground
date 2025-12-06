//object method 
let myPerson ={
    name:"priya",
    age:21,
    IsInCollege:true,
    address:{
        city:"Noida",
        NearBy:"Metro station"
    },
    hobbies:["gym","walking","coffee"],
    greet:function(){
        console.log("hello world")
    }

}

console.log(myPerson)

//object.keys

// *console.log(Object.keys(myPerson))


//object.values

//* console.log(Object.values(myPerson))

// object.entries
// *console.log(Object.entries(myPerson))


// object.assign

//* let a = {x:1}
// *let b = {y:2}
// *let c = {a,b}
// *console.log(c)





//* let a = {x:1}
// *let b ={y:2}
// *let c = Object.assign({},a,b)

// *console.log(c)


// freeze

let obj = {theme:"dark"};

Object.freeze(obj);
obj.theme = "light"
console.log(obj.theme)