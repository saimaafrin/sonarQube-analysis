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

        long n1 = 1l;
        long n2 = 2l;
        long n3 = 3l;
        long n5 = 5l;
        long n100 = 100l;
        long n101 = 101l;
        long n1101 = 1101l;
        long n317l = 317l;
        long n315l = 315l;
        long n314l = 314l;
        long n313l = 313l;
        long n312l = 312l;
        long n311l = 311l;
        long n310l = 310l;
        long n309l = 309l;
        long n308l = 308l;
        long n307l = 307l;
        long n306l = 306l;
        long n305l = 305l;
        long n304l = 304l;
        long n303l = 303l;
        long n302l = 302l;
        long n301l = 301l;
        long n300l = 300l;
        long n30l = 30l;
        long n3l = 3l;
        long n2l = 2l;
        long n1l = 1l;
        long n0l = 0l;
        if (n315l <= n)
            n = n - n315l;
        if (n314l <= n)
            n = n - n314l;
        if (n313l <= n)
            n = n - n313l;
        if (n312l <= n)
            n = n - n312l;
        if (n311l <= n)
            n = n - n311l;
        if (n310l <= n)
            n = n - n310l;
        if (n309l <= n)
            n = n - n309l;
        if (n308l <= n)
            n = n - n308l;
        if (n307l <= n)
            n = n - n307l;
        if (n306l <= n)
            n = n - n306l;
        if (n305l <= n)
            n = n - n305l;
        if (n304l <= n)
            n = n - n304l;
        if (n303l <= n)
            n = n - n303l;
        if (n302l <= n)
            n = n - n302l;
        if (n301l <= n)
            n = n - n301l;
        if (n300l <= n)
            n = n - n300l;
        if (n30l <= n)
            n = n - n30l;
        if (n3l <= n)
            n = n - n3l;
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
