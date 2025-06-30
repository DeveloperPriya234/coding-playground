function addNums(...numbers){
  return  numbers.reduce((acc , curr)=>{
        return acc + curr
    })
}

console.log(addNums(123,45,6,7,8,9,0))