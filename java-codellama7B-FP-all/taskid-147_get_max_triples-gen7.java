import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a positive integer n. You have to create an integer array array list a of length n.
    // For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    // Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    // and a[i] + a[j] + a[k] is a multiple of 3.
    // Example :
    // >>> getMaxTriples((5l))
    // (1l)
    // Explanation: 
    // a = [1, 3, 7, 13, 21]
    // The only valid triple is (1, 7, 13).
    public static long getMaxTriples(long n) {

        return LongStream.rangeClosed(1, n).boxed()
                .filter(i -> isMultipleOf3(i * i - i + 1))
                .mapToObj(Long::valueOf)
                .map(i -> Pair.with(i, Pair.with(i, i)))
                .reduce((p1, p2) -> {
                    long i1 = p1.getValue0().getValue0().longValue();
                    long i2 = p2.getValue0().getValue0().longValue();
                    long v1 = p1.getValue1().getValue0().longValue();
                    long v2 = p2.getValue1().getValue0().longValue();
                    return i1 > i2 ? p1 : v1 > v2 ? p2 : p1;
                })
                .map(p -> (p.getValue0().getValue0().longValue() * 2 + 1) * p.getValue0().getValue0().longValue() / 3)
                .orElse(0l);
    }
    public static void main(String[] args) {
    assert(getMaxTriples((5l)) == (1l));
    assert(getMaxTriples((6l)) == (4l));
    assert(getMaxTriples((10l)) == (36l));
    assert(getMaxTriples((100l)) == (53361l));
    }

}
