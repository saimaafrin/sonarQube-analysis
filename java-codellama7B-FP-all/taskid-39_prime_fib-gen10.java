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

        if (n == (1l)) {
            return (2l);
        }
        long a = (1l);
        long b = (1l);
        long c = (0l);
        while (n > (1l)) {
            long a2 = (a * (a + (1l)));
            long b2 = (b * (b + (1l)));
            long c2 = (c * (c + (1l)));
            if ((a2) % ((2l) * (a) + (1l)) == (0l)) {
                a = (b);
                b = (c);
                c = (a2 / (2l));
            } else {
                a = (a2 + (1l));
                b = (b2 + (1l));
                c = (c2 + (1l));
            }
            n = (n - (1l));
        }
        return (c);
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
