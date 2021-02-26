//function that accepts a number
//return the factorial of number
const factorial = ((num) => {
    if (num === 0) {
        return 1
    } else {
        return num * factorial(--num);
    }
})

console.log(factorial(5))