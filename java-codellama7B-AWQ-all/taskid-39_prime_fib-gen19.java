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

        // fibonacci returns n-th number of Fibonacci series
        // >>> fibonacci((1l))
        // (1l)
        // >>> fibonacci((2l))
        // (1l)
        // >>> fibonacci((3l))
        // (2l)
        // >>> fibonacci((4l))
        // (3l)
        // >>> fibonacci((5l))
        // (5l)
        // >>> fibonacci((6l))
        // (8l)
        // >>> fibonacci((7l))
        // (13l)
        // >>> fibonacci((8l))
        // (21l)
        // >>> fibonacci((9l))
        // (34l)
        // >>> fibonacci((10l))
        // (55l)
        // >>> fibonacci((11l))
        // (89l)
        // >>> fibonacci((12l))
        // (144l)
        // >>> fibonacci((13l))
        // (233l)
        // >>> fibonacci((14l))
        // (377l)
        long fibonacci = (long) Math.floor(Math.sqrt(5*n+0.5));
        long a = 0;
        long b = 1;
        long c = 0;
        long d = 1;
        while (c<n) {
            a = b;
            b = c;
            c = a+b;
            d = b+c;
        }
        // >>> isPrime(a)
        // (true)
        // >>> isPrime(b)
        // (true)
        // >>> isPrime(c)
        // (true)
        // >>> isPrime(d)
        // (true)
        if (c>n) {
            if (isPrime(b)) return b;
            if (isPrime(c)) return c;
        } else {
            if (isPrime(c)) return c;
            if (isPrime(d)) return d;
        }
        return 0;
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
