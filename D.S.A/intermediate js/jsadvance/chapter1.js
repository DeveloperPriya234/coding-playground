//json
//!json javascript object notation is a interchange format that is:
//?human-readable
//?easy for machines to parse and generate
//? language independent (although it is based on an subset of javascript syntax)

//*example


// {
//     "name":"priya",
//     "age":21,
//     "isStudent":true,
//     "skills":["javascript","python"],
//     "address":{
//         "city":"delhi",
//         "pincode":110001

    
//     }


// }

// why json is not a part of javascript?

//!JSON is a data format not a language feature
//!it has stricter syntax rules

//*all keys must be in double quotes
//*only primitive values arrays or nested json objects allowed
//*cannot include functions undefined comments or symbol..

//json was made language-agnostic
//*designed for data exchange between language
//*can be used in python,java,php,ruby,etc..


//? that's why JSON is not just a javascript thing even through it originated from js

// why do we need JSON in javascript??
//! data exchange with apis

//?most modern web applications communicate with backends using http request where data is sen receive is json format..

//storage and configuration
//* used in config files(`package,json`)

//*storing data in `localstorage` or `sessionStorage`(which can only store strings)


//serialization and deserialization

//*convert objects to strings (for storage or network transmission)

//*convert strings back to usable js objects

