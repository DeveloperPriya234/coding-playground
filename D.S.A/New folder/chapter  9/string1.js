//string;
//immutable;
//primitive data type;
//sequence of characters;



//what is string in js?
//!String is a primitive data type in JavaScript that represents a sequence of characters. Strings are immutable, meaning once they are created, their values cannot be changed. However, you can create new strings based on existing ones using various string methods.

//Creating strings?
//!You can create strings in JavaScript using single quotes (' '), double quotes (" "), or backticks (` `) for template literals


// let str1 = "Hello, World!🐦‍🔥"; // double quotes

// console.log(str1[9])
// console.log(str1[-1])

// str1[0]= "u" //?it will not change the string because string is immutable
// console.log(str1)
// console.log(str1.length)
// console.log(str1.charAt(9))



// let str2 = 'JavaScript is fun!🚀'; // single quotes
// console.log(str1+" "+str2)

// let str3 = `Template literals allow for multi-line strings and interpolation: ${str1.str2}`;

// console.log(str3)
//  // backticks



// let str4 = new String("String object"); // using String constructor






//string properties;

// *str2 = "JavaScript is fun!🚀"
// *console.log(`${str1} ${str2}`);
// *console.log(`${20+30}`);

// *"let str1 = "Hello, World!🐦‍🔥";
// *console.log(str1.length);


// *console.log(str1[7])"

// *let str2 ="🚀";
// *console.log(str2.length);



//string methods;
//!String methods are built-in functions that allow you to manipulate and interact with string data in JavaScript. Here are some commonly used string methods:

// charAt();
//!.returns the character at the specified index
// *let str1 = "Hello, World!🐦‍🔥";
// *console.log(str1.charAt(7)); // W

//charCodeAt();
//!.returns the Unicode of the character at the specified index
// *let str1 = "Hello, World!🐦‍🔥";
// *console.log(str1.charCodeAt(7)); // 87
// *console.log(str1.charCodeAt(13)); // 128038


//slice(starting,ending);
//!.extracts a section of a string and returns it as a new string
// *let str1 = "helloworld";
// *console.log(str1.slice(5,10)); // World
//* console.log(str1.slice(0,5)); // Hello
// *console.log(str1.slice(-5)); // World
// *console.log(str1.slice(2,-3)); // llowo


//substring(starting,ending);
//!.returns the part of the string between the start and end indexes, or to the end of the string doest not accept negative indexes
// *let str1 = "helloworld";
// *console.log(str1.substring(5,10)); // World
//* console.log(str1.substring(0,5)); // Hello
// *console.log(str1.substring(2)); // lloworld


//substr(starting,length);
//!.returns the part of the string starting from the specified index and extending for a given number of characters
// *let str1 = "helloworld";
// *console.log(str1.substr(5,5));
// *console.log(str1.substr(0,5));
// *console.log(str1.substr(-5,5));
// *console.log(str1.substr(2,5));
// *console.log(str1.substr(0))



//uppercase();
//!.converts the string to uppercase letters
// *let str1 = "Hello, World!";
// *console.log(str1.toUpperCase());


// *let str2 = "JavaScript is fun!";
// *console.log(str2.toUpperCase());



//lowercase();
//!.converts the string to lowercase letters
//* let str1 = ("HELLO WORLD!");
// *console.log(str1.toLowerCase());

// *let str2 = "JAVASCRIPT IS FUN!";
// *console.log(str2.toLowerCase());


