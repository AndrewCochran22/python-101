//function called productOfArray
//array of numbers as input
//return product of array
const productOfArray = (arr) => {
    let total = 1;
    if (arr.length === 0) {
        return total;
    } else {
        total = arr[0] * productOfArray(arr.slice(1));
        return total;
    }
}

console.log(productOfArray([1, 2, 3, 4]));