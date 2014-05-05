/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

var start_time = Date.now(),
    answer,
    end_time,
    factors,
    num = 600851475143;

// Code here

// Sieve of Eratosthenes
function prime_factors(n) {
    var i = 2,
        factors = [];
    while (i * i <= n) {
        if (n % i) {
            i += 1;
        } else {
            n = Math.floor(n / i);
            factors.push(i);
        }
    }
    if (n > 1) {
        factors.push(n);
    }
    return factors;
}

factors = prime_factors(num);
answer = factors[factors.length - 1];

// End timer
end_time = Date.now();

console.log('Answer: ', answer);
console.log('Execution Time: ', end_time - start_time);
