
// methods of array
// push(),
// !.adds items(s) to the end of an array
// *let num1 = [10,20,30];
// *num1.push(67)
// *console.log(num1);

// pop(),
// !.removes the last item from an array
//* let result = num1.pop();
// *console.log(result);
// *console.log(num1);

// shift(),
// !.removes the first item from an array
// *let shift = num1.shift();
// *console.log(shift);
// *console.log(num1);

// unshift(),
// !.adds items(s) to the beginning of an array
//* let unshiftitem = num1.unshift(5);
// *console.log(unshiftitem);
// *console.log(num1);

// length;
//* console.log(num1.length);

//splice(remove.replace.insert);
//!.remove items from an array

//* let num =[10,20,30,40,50];
//* num.splice(1,2)
// *console.log(num);
// ?replace items in an array
// *num.splice(0,2,78,98);
// *console.log(num);

//?insert items in an array
// *num.splice(2,0,100,200);
// *console.log(num);

//sort();
//!.sort the items of an array in ascending order
// *let num =[50,20,30,10,40];
//* num.sort();
// *console.log(num);

//reverse();
//!reverse the array in the place
// *let num =[10,20,30,40,50];
// *num.reverse();
// *console.log(num);

//accessor/non mutable methods
//concat();
//!.joins two or more arrays and returns a new array

//? slice(end,start);
//!.returns selected elements in an array as a new array
// *let num = [10,20,30,40,50];
// *let result = num.slice(0,3);
// *console.log(result);
// *console.log(num);
//*let num = [7,8,9,7,4,5]
//*let result = num.slice(1,4)
//*console.log(result);

//concat();
//!.joins two or more arrays and returns a new array

// *let num = [10,20,30,40,50];
// *let num2 = [60,70,80,90,100];
// *let result = num.concat(num2);
// *console.log(result);
// *console.log(num);
// *console.log(num2);

// includes();(value);
//!.checks if an array contains a specified element and returns true or false
//* let num = [10,20,30,40,50];
// *let result = num.includes(30);
// *console.log(result);
// *console.log(num);   


// *let transport = ['car','bus','bike','train'];
// *let result = transport.includes('plane');
// *console.log(result);
// *console.log(transport);



// indexOf();(value);
//!.returns the first index at which a given element can be found in the array, or -1 if it is not present
// *let num = [10,20,30,40,50];
// *let result = num.indexOf(30);
// *console.log(result);
// *console.log(num);

// join(separator);
//!.joins all elements of an array into a string
// *let num = [10,20,30,40,50];
// *let result = num.join('-');
// *console.log(result);
// *console.log(num);