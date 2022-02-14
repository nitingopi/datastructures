class Recursion {

    factorialWithRecursion(n) {
        if (n == 0) {
            return 1;
        }

        return n * this.factorialWithRecursion(n - 1);
    }

    factorialWithoutRecursion(n) {
        let factorial = 1;
        for (let v = n; v >= 1; v--) {
            factorial *= v;
        }
        return factorial;
    }
}

const obj = new Recursion();
result = obj.factorialWithRecursion(9);
console.log(result);
result = obj.factorialWithoutRecursion(9);
console.log(result);