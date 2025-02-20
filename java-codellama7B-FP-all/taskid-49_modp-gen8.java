import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return 2^n modulo p (be aware of numerics).
    // >>> modp((3l), (5l))
    // (3l)
    // >>> modp((1101l), (101l))
    // (2l)
    // >>> modp((0l), (101l))
    // (1l)
    // >>> modp((3l), (11l))
    // (8l)
    // >>> modp((100l), (101l))
    // (1l)
    public static long modp(long n, long p) {

        // Long division of 2^n by p.
        long res = 1;
        long pow = n;
        while (pow != 0) {
            if (pow % 2 != 0) {
                res = res * 2 % p;
            }
            pow = pow / 2;
            n = n * n % p;
        }
        return res;
    }
    public static void main(String[] args) {
    assert(modp((3l), (5l)) == (3l));
    assert(modp((1101l), (101l)) == (2l));
    assert(modp((0l), (101l)) == (1l));
    assert(modp((3l), (11l)) == (8l));
    assert(modp((100l), (101l)) == (1l));
    assert(modp((30l), (5l)) == (4l));
    assert(modp((31l), (5l)) == (3l));
    }

}
