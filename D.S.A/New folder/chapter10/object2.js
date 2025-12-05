// singleton
// Object.create  //*constructuor method
// objects literals
const mySym = Symbol("key1")

const jsUser = {
    name: "priya",
    age: 18,
    location: "noida",
    email: "priya234@gmail.com",
    isLoggedIn:false,
    LastLoginDays: ["monday","saturday"],
    [mySym]: "key1",
}



console.log(typeof(jsUser[mySym]))
console.log(jsUser.email)
console.log(jsUser["email"])


jsUser.email = "priya123@gmail.com"

console.log(jsUser["email"])

Object.freeze(jsUser)
jsUser.email="priya222@gmail.com"
console.log(jsUser["email"])