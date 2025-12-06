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
console.log(Object.entries(myPerson))