import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given an array array list arr of integers and you need to return
    // sum of magnitudes of integers multiplied by product of all signs
    // of each number in the array array list, represented by 1, -1 or 0.
    // Note: return null for empty arr.
    // Example:
    // >>> prodSigns((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)2l, (long)-4l))))
    // 9l
    // >>> prodSigns((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l))))
    // 0l
    // >>> prodSigns((new ArrayList<Long>(Arrays.asList())))
    // Optional.empty()
    public static Optional<Long> prodSigns(ArrayList<Long> arr) {

        if (arr.size() == 0) {
            return Optional.empty();
        }
        long product = 1;
        for (Long i : arr) {
            product *= (i < 0 ? -1 : 1);
        }
        long result = 0;
        for (Long i : arr) {
            result += Math.abs(i) * product;
        }
        return Optional.of(result);
    }
    public static void main(String[] args) {
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)2l, (long)-4l)))).equals(-9l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l)))).equals(0l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)1l, (long)1l, (long)1l, (long)2l, (long)3l, (long)-1l, (long)1l)))).equals(-10l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList()))).equals(Optional.empty()));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)1l, (long)2l, (long)-1l, (long)-1l, (long)9l)))).equals(20l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)-1l, (long)1l, (long)-1l, (long)1l)))).equals(4l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)-1l, (long)1l, (long)1l, (long)1l)))).equals(-4l));
    assert(prodSigns((new ArrayList<Long>(Arrays.asList((long)-1l, (long)1l, (long)1l, (long)0l)))).equals(0l));
    }

}
