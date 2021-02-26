//ask user for numerical input n
//print fibonacci values from 0 to n
let n = 9;

const fibonacci = (n) => {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(n))