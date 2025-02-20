import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    // >>> primeFib((1l))
    // (2l)
    // >>> primeFib((2l))
    // (3l)
    // >>> primeFib((3l))
    // (5l)
    // >>> primeFib((4l))
    // (13l)
    // >>> primeFib((5l))
    // (89l)
    public static long primeFib(long n) {

        // fibonacci numbers
        long[] fib = new long[]{(long) 0, (long) 1, (long) 1, (long) 2};
        // current Fibonacci number
        long curFib = (long) 2;
        // i is the index of fib
        long i = (long) 2;
        // n-th fibonacci number
        long res = (long) 0;
        // n-th number
        long num = (long) 0;
        // temp
        long temp = (long) 0;
        // max n
        long max = (long) 50;
        // max prime
        long maxPrime = (long) 50;
        // get n-th prime
        do {
            // get n-th prime
            temp = getPrime(max);
            // add to the array of prime numbers
            fib[i] = temp;
            // set curFib to temp
            curFib = temp;
            // add to the index
            i = i + 1;
            // set max
            max = max + 1;
            // set maxPrime
            maxPrime = maxPrime + 1;
            // get prime number
        } while (i < maxPrime);
        // get the n-th prime number
        res = fib[n];
        // set num to res
        num = res;
        // do while prime
        do {
            // set num to num + 1
            num = num + (long) 1;
            // get prime number
        } while (!isPrime(num));
        // return the number
        return num;
    }
    public static void main(String[] args) {
    assert(primeFib((1l)) == (2l));
    assert(primeFib((2l)) == (3l));
    assert(primeFib((3l)) == (5l));
    assert(primeFib((4l)) == (13l));
    assert(primeFib((5l)) == (89l));
    assert(primeFib((6l)) == (233l));
    assert(primeFib((7l)) == (1597l));
    assert(primeFib((8l)) == (28657l));
    assert(primeFib((9l)) == (514229l));
    assert(primeFib((10l)) == (433494437l));
    }

}
