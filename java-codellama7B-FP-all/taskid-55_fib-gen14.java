import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return n-th Fibonacci number.
    // >>> fib((10l))
    // (55l)
    // >>> fib((1l))
    // (1l)
    // >>> fib((8l))
    // (21l)
    public static long fib(long n) {

        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        long pre = 0;
        long cur = 1;
        long res = 1;
        for (long i = 2; i <= n; i++) {
            res = cur + pre;
            pre = cur;
            cur = res;
        }
        return res;
    }
    public static void main(String[] args) {
    assert(fib((10l)) == (55l));
    assert(fib((1l)) == (1l));
    assert(fib((8l)) == (21l));
    assert(fib((11l)) == (89l));
    assert(fib((12l)) == (144l));
    }

}
