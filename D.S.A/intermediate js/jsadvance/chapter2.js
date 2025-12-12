let myObj ={
    name:"john",
    age:30,
    iaAdmin:true,
    isKiller:false,
    address:{
        city:"Noida",
        nearBy:"metro station"
    }
}

//object -----> JSON(JSON.stringify())
let strObj = JSON.stringify(myObj);
console.log(strObj)
console.log(typeof(strObj))
//json ----->object (JSON.parse())

let myJSON=`{
    "name":"priya",
    "age":20,
    "isAdmin":true,
    "address":{
        "city":"Noida",
        "nearBy":"metro station"
    }


}`

let myNewObj = JSON.parse(myJSON)
console.log(myNewObj)