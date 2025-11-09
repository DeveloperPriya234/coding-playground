age = 56;
if (age< 0){
    console.log("this is invalid age");
}
else if (age<9){
    console.log("you are a kid and you cannot even think of driving");
}

else if (age<18 && age>=9){
    console.log("you are a teen and you can think of driving after 18");
}

else{
    console.log("you are eligible for driving");
}

console.log("end of program");


//explore switch statements and write a basic program in the comments;

console.log("you can",(a<18? "not drive":"drive"));