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

        long n1 = n - 1;
        long n2 = n - 2;
        long n3 = n - 3;
        long n4 = n - 4;
        long a = 0;
        long b = 0;
        long c = 2;
        long d = 0;
        long ans = 0;
        while (n4 >= 0) {
            ans = (ans + a) % 1000000007;
            long tmp = a;
            a = (a + b + c + d) % 1000000007;
            b = (b + c) % 1000000007;
            c = (c + d) % 1000000007;
            d = (tmp + n1) % 1000000007;
            n1 = n2;
            n2 = n3;
            n3 = n4;
            n4 = n4 - 4;
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(fib4((5l)) == (4l));
    assert(fib4((8l)) == (28l));
    assert(fib4((10l)) == (104l));
    assert(fib4((12l)) == (386l));
    }

}
