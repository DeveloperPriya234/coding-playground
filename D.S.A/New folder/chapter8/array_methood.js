//for each 
//! The forEach() method executes a provided function once for each array element.
// *let num = [10, 20, 30, 40, 50];
//* num.forEach((value,index,array)=>{console.log("the value is ",value+"and the index is",+index)
// *    console.log(array)
// *})

//* let result = [1,2,3,4,5,6,7,8,9,10];
// *result.forEach((value,index,array)=>{console.log(value*2+"at the value of "+value)
//  *   console.log(array)
//* })

// *let num = [10, 20, 30, 40, 50];
// *num.forEach(function (value, index, array) {
// *    console.log('Value:', value, 'Index:', index, 'Array:', array);
//* let num_join = num.join('-');
// *console.log(num_join);

// *});


// *let numbers = [1,2,3,4,5,6,7,8,9,10];
//* numbers.forEach((value,index,array)=>{console.log(value*3+" at the index of "+index)})

//* let num = [1,2,3,4,5,6,7,8,9,10];
// *num.forEach(function (value, index, array) {
//  *   console.log(`2 x ${index+1} = ${value*2}`);
//* });


//map method
//! The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.
//* let numbers = [1,2,3,4,5,6,7,8,9,10];
//* let result = numbers.map((value,index,array)=>{return value*2})
// *console.log(result)


//filter
//! The filter() method creates a new array with all elements that pass the test implemented by the provided function.
//* let numbers = [1,2,3,4,5,6,7,8,9,10];
// *let result = numbers.filter((value,index,array)=>{return value>5

//* })
// *console.log(result)

//reduce
//! The reduce() method executes a reducer function (that you provide) on each element of the array, resulting in a single output value.

// *let numbers = [1,2,3,4,5,6,7,8,9,10];
// *let result = numbers.reduce((accumulator,currentValue,index,array)=>{
// *return accumulator+currentValue
// *},0)
//* console.log(result)

//* let price = [1,2,3,4,5];
// *let total = price.reduce((accumulator,currentValue,index,array)=>{
//  *   return accumulator*currentValue
// *},1)
// *console.log(total)

//find
//! The find() method returns the value of the first element in the provided array that satisfies the provided testing function.
//* let numbers = [1,2,3,4,5,6,7,8,9,10];
//* let result = numbers.find((value,index,array)=>{return value>5})
//* console.log(result)
