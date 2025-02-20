import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    // fibfib(0) == 0
    // fibfib(1) == 0
    // fibfib(2) == 1
    // fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    // Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    // >>> fibfib((1l))
    // (0l)
    // >>> fibfib((5l))
    // (4l)
    // >>> fibfib((8l))
    // (24l)
    public static long fibfib(long n) {

        if (n == 0l) return 0l;
        if (n == 1l) return 0l;
        if (n == 2l) return 1l;
        long k = (long) Math.floor(Math.sqrt(5*n+0.25));
        long d = (k*k - n) / 5;
        long f = (k*(k+1) - n) / 5;
        return f + d*(f + f + 1);
    }
    public static void main(String[] args) {
    assert(fibfib((2l)) == (1l));
    assert(fibfib((1l)) == (0l));
    assert(fibfib((5l)) == (4l));
    assert(fibfib((8l)) == (24l));
    assert(fibfib((10l)) == (81l));
    assert(fibfib((12l)) == (274l));
    assert(fibfib((14l)) == (927l));
    }

}
