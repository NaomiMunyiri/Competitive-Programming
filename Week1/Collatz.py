const collatz = (num) => {

    var steps = 0;

    while (num !== 1 && num > 0) {
        if (num % 2 === 0) {
            num = num/2;
            steps++; 
        } else if (num%2 !== 0){ 
            num = 3*num +1;
            steps++;
        }
    }
    return steps;
}

n=n/2 if n%2==0 else 3*n +1
n