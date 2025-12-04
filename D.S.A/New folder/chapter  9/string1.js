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


//includes();
//!.determines whether one string may be found within another string, returning true or false as appropriate
// *let str1 = "Hello, World!";
// *console.log(str1.includes("World")); // true
// *console.log(str1.includes("world")); // false

// *let str2 = "javascript is fun!";
// *console.log(str2.includes("is")); // true
// *console.log(str2.includes(" "))// true
// *console.log(str2.includes("java")); // false    
// *console.log(str2.includes("fun!")); // true
// *console.log(str2.includes("Python")); // false


//startsWith();
//!.determines whether a string begins with the characters of a specified string, returning true or false as appropriate
//* let str1 = "Hello, World!";
// *console.log(str1.startsWith("Hello")); // true
// *console.log(str1.startsWith("World")); // false


//* let str2 = "hello world i am learning javascript";
//* console.log(str2.startsWith("hello"))
//* console.log(str2.startsWith("h"))

//endsWith();
//!.determines whether a string ends with the characters of a specified string, returning true or false as appropriate
// *let str1 = "Hello, World!";
// *console.log(str1.endsWith("!")); // true
// *console.log(str1.endsWith("World")); // false


//endsWith();
//!.determines whether a string ends with the characters of a specified string, returning true or false as appropriate
//* let string = "hello world i am learning javascript";
//* console.log(string.endsWith("javascript"))
// *console.log(string.endsWith("script"))
//* console.log(string.endsWith("t"))
// *console.log(string.endsWith("hello"))


//* let str2 = "I love JavaScript. JavaScript is fun!";
// *console.log(str2.startsWith("I"))
// *console.log(str2.endsWith("fun!"))

//replace(searchValue, newValue);
//!.returns a new string with some or all matches of a pattern replaced by a replacement



// let str1 = "Hello, World!";
// let newStr1 = str1.replace("World", "JavaScript");
// console.log(newStr1); // Hello, JavaScript!


// let str2 ="banana  apple banana grape banana";
// let newStr2 = str2.replace("banana", "orange");
// console.log(newStr2); // orange apple banana grape banana

//?replaces the first match by default(use regex with g flag of all)


// *let str2 = ("apple banana papaya apple cheery")
// *let newStr2 = str2.replace(/apple/g, "grapes"

// *)

// *console.log(newStr2)



//trim;
//!removes extra whitespaces from both ends of string
// *let string = ("    hello world  ")
// *let newString = string.trim();
// *console.log(newString);


// *let string = ("   hello world  ");
// *let newString = string.trimStart();
// *console.log(newString)

//* let string = ("    hello world     ")
// *let newString = string.trimEnd();
// *console.log(newString)

//split
//* let string = ("red,green,yellow,purple,black")
// *let newString = string.split(",");
// *console.log(newString)


// repeat(n);

// *let string = ("hello ")
// *let newString = string.repeat(20)
// *console.log(newString)


//concat
// *let string = ("hello");
// *let string2= ("world");
// *let newString = string.concat(string2)
//* console.log(newString)


// console.log("hello ".repeat(10000));

