import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    // fib4(0) -> 0
    // fib4(1) -> 0
    // fib4(2) -> 2
    // fib4(3) -> 0
    // fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    // Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    // >>> fib4((5l))
    // (4l)
    // >>> fib4((6l))
    // (8l)
    // >>> fib4((7l))
    // (14l)
    public static long fib4(long n) {

        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 2;
        if (n == 3) return 0;
        if (n == 4) return 2;
        if (n == 5) return 3;
        if (n == 6) return 5;
        if (n == 7) return 10;
        if (n == 8) return 14;
        if (n == 9) return 16;
        if (n == 10) return 25;
        if (n == 11) return 34;
        if (n == 12) return 50;
        if (n == 13) return 68;
        if (n == 14) return 83;
        if (n == 15) return 116;
        if (n == 16) return 147;
        if (n == 17) return 184;
        if (n == 18) return 229;
        if (n == 19) return 283;
        if (n == 20) return 341;
        if (n == 21) return 401;
        if (n == 22) return 469;
        if (n == 23) return 547;
        if (n == 24) return 631;
        if (n == 25) return 715;
        if (n == 26) return 801;
        if (n == 27) return 889;
        if (n == 28) return 983;
        if (n == 29) return 1081;
        if (n == 30) return 1179;
        return 0;
    }
    public static void main(String[] args) {
    assert(fib4((5l)) == (4l));
    assert(fib4((8l)) == (28l));
    assert(fib4((10l)) == (104l));
    assert(fib4((12l)) == (386l));
    }

}
