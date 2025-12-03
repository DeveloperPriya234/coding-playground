//iteration methods
//forEach();
//!.executes a provided function once for each array element
let num = [10, 20, 30, 40, 50];
num.forEach(function (value, index, array) {
    console.log('Value:', value, 'Index:', index, 'Array:', array);
});

//filter();
//!.creates a new array with all elements that pass the test implemented by the provided function
let numbers = [5, 12, 8, 130, 44];  
let filteredNumbers = numbers.filter(function(value) {
    return value > 10;
});
console.log(filteredNumbers); // [12, 130, 44]
//map();
//!.creates a new array populated with the results of calling a provided function on every element in the calling array
let mappedNumbers = numbers.map(function(value) {
    return value * 2;
}
);
console.log(mappedNumbers);
//reduce();
//!.executes a reducer function on each element of the array, resulting in a single output value
let sum = numbers.reduce(function(accumulator, currentValue) {
    return accumulator + currentValue;
}, 0);
console.log(sum); // 199
//some();
//!.tests whether at least one element in the array passes the test implemented by the provided function

let hasLargeNumber = numbers.some(function(value) {
    return value > 100;
});
console.log(hasLargeNumber);
//every();
//!.tests whether all elements in the array pass the test implemented by the provided function
let allLargeNumbers = numbers.every(function(value) {
    return value > 3;
});
console.log(allLargeNumbers);
//find();
//!.returns the value of the first element in the array that satisfies the provided testing function
let foundNumber = numbers.find(function(value) {
    return value > 10;
});
console.log(foundNumber); // 12
//findIndex();
//!.returns the index of the first element in the array that satisfies the provided testing function
let foundIndex = numbers.findIndex(function(value) {
    return value > 10;
});