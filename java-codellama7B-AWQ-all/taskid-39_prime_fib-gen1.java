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

        long[] fib = {0, 1};
        long[] p = {0, 1};
        for (int i = 2; i < n; i++) {
            long a = fib[i - 1] + fib[i - 2];
            long b = a - fib[i - 1];
            long c = a * b;
            long d = c - b;
            long e = c * d;
            long f = e - d;
            fib[i] = f;
            p[i] = 1;
            for (int j = 2; j < i; j++) {
                if (f % p[j] == 0) {
                    p[i] = p[j];
                    break;
                }
            }
            if (p[i] == 1) {
                return fib[i];
            }
        }
        return -1;
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
