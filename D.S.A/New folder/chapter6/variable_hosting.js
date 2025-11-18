// variable hosting
console.log(a); // undefined
var a = 5;
console.log(a); // 5


// function hosting
console.log(sum(2, 3));
function sum(x, y) {
    return x + y;
}
// Output:
// undefined
// 5
// 5    
// 5
console.log(sum(2, 3)); // 5
console.log(sum(2, 3)); // 5
console.log(sum(2, 3)); // 5
console.log(sum(2, 3)); // 5
console.log(sum(2, 3)); // 5
