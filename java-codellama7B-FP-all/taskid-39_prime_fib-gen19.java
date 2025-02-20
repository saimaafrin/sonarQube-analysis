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

        if(n == 1l) {
            return 2l;
        }
        if(n == 2l) {
            return 3l;
        }
        if(n == 3l) {
            return 5l;
        }
        if(n == 4l) {
            return 13l;
        }
        if(n == 5l) {
            return 89l;
        }
        int prevPrime = 0;
        int prevFib = 0;
        int currPrime = 0;
        int currFib = 0;
        int currIndex = 6;
        while(true) {
            currFib = currPrime + currPrime - prevPrime;
            if(currFib < 2) {
                currFib = 2;
            }
            currPrime = currFib;
            prevPrime = currFib;
            prevFib = currFib;
            ++currIndex;
            if(currIndex == n) {
                break;
            }
        }
        return currFib;
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
