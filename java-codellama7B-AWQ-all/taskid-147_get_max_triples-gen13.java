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

        int max = (int) n;
        int i = 1, j = 2, k = 3;
        int[] a = new int[max + 1];
        for (int i1 = 1; i1 <= max; i1++) {
            a[i1] = i1 * i1 - i1 + 1;
            i = i1;
            if (i1 >= j && i1 >= k) {
                j = i1;
            }
            if (i1 >= k) {
                k = i1;
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int i2 = 1; i2 <= max; i2++) {
            if (a[i2] % 3 == 0 && i2 != i && i2 != j && i2 != k) {
                list.add(a[i2]);
            }
        }
        return list.size();
    }
    public static void main(String[] args) {
    assert(getMaxTriples((5l)) == (1l));
    assert(getMaxTriples((6l)) == (4l));
    assert(getMaxTriples((10l)) == (36l));
    assert(getMaxTriples((100l)) == (53361l));
    }

}
