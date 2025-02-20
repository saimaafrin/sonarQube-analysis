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

        long[][] fib = new long[n+1][2];
        fib[0] = new long[]{0l, 1l};
        for (int i=1; i<=n; i++) {
            fib[i] = new long[]{fib[i-1][0]+fib[i-1][1], fib[i-1][0]};
        }
        long[] pf = new long[n+1];
        pf[1] = 2l;
        for (int i=2; i<=n; i++) {
            for (int j=0; j<i; j++) {
                if (fib[i][0] % fib[j][0] == 0) {
                    pf[i] = 0l;
                    break;
                }
                if (fib[i][1] % fib[j][0] == 0) {
                    pf[i] = 0l;
                    break;
                }
            }
            if (pf[i] != 0l) {
                pf[i] = fib[i][0];
            }
        }
        return pf[n];
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
