/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

var start_time = Date.now(),
    answer,
    end_time,
    largest = 0,
    product;

// Code here
for (var i = 100; i <= 999; i++) {
    for (var j = 100; j <= 999; j++) {
        product = i * j;
        if (product.toString().split("").reverse().join("") === product.toString() && product > largest) {
            largest = product;
        }
    }
}

// End timer
end_time = Date.now();

console.log('Answer: ', largest);
console.log('Execution Time: ', end_time - start_time);
