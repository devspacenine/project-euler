/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
 */

var start_time = Date.now(),
    answer,
    end_time;

// Code here
answer = 0;
x = 1;
while (true) {
    if (x % 3 === 0 || (x % 5 === 0 && x % 3 !== 0)) {
        answer += x;
    }
    if (++x >= 1000) {
        break;
    }
}

// End timer
end_time = Date.now();

console.log('Answer: ', answer);
console.log('Execution Time: ', end_time - start_time);
