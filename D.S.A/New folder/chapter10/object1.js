// object 
// !in javascript, **objects** are collections of key- value pairs.
//!keys are always strings (or symbol),and values can be any type...

//* let myPerson = {
//  *   name:"priya",
//    * age:21,
//   *  isInCollege:true,
//    * address:{
//       *  city:"noida",
//      *   nearBy:"metro station",
//   *  },
//   *  hobbies:["gym","walking","coffee"],
//   *  greet:function(){
//   *  console.log("hello world")
// *}
// *}

// *myPerson.diet = ["maggie","fast food", "mommos","noodles","pizza"]
 //1st way
// ?console.log(myPerson) 
// ?console.log(myPerson.greet())
// ?console.log(myPerson.hobbies) 
// ?console.log(myPerson.address.city) 


//2nd way
//? console.log(myPerson["hobbies"])



// *const myNewObj = new Object()
// *myNewObj.name = "priya";
// *myNewObj.location = "noida";
// *myNewObj.biecepsSize = 10;

// *console.log(myNewObj)


// *const proto = {greet(){console.log("hii");}};
// *const obj = object.create(proto);
// *obj.greet(); 



//singleton
//! singleton is an object that is created once and used globally across your code. it's useful when you want to ensure only one instance of an object ..

//! singleton is an object that is created once and used globally across your code.its useful when you want to ensure only one instance of an object..

//! singleton is an object that is created once and used globally across code. it's useful when you want to ensure only one instance of an object..

//! singleton is an object that is created once and used globally used across code. it's useful when you want to ensure only one instance of an object..


//!singleton is an object that is created once and used globally used across code. it's useful when you want to ensure only one instance of an object 


//! singleton is an object that is created once and used globally used across code..it's useful when you want to ensure only one instance of an object..


//!singleton is an object that is created once and used globally used across code.it's useful when you want to ensure only one instance of an object..


//! singleton is an object that is created once and used globally used across code. it's useful when you want to ensure only one instance of an object..


//! singleton is an object that is created once and used globally used across code.it's useful when you want to ensure only one instance of an object..

//! singleton is an object that is created once and used globally used across code it's useful when you want ensure only one instance of an object..

//! singleton is an object that is crated once and used globally used across code its useful when you want ensure only one instance of an object


const TeddyBear = (function(){
    let onlyOneBear;

    function createdTeddy(){
        return{name:"fluffy"};
    }

    return{
        getBear:function(){
            if(!onlyOneBear){
                onlyOneBear = createdTeddy();
            }
            return onlyBear
        }
    }
})();

const myBear1 = TeddyBear.getBear();
const myBear2 = TeddyBear.getBear();


console.log(myBear1);