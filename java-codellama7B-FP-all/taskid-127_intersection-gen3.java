import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given two intervals,
    // where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    // The given intervals are closed which means that the interval (start, end)
    // includes both start and end.
    // For each given interval, it is assumed that its start is less or equal its end.
    // Your task is to determine whether the length of intersection of these two 
    // intervals is a prime number.
    // Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    // which its length is 1, which not a prime number.
    // If the length of the intersection is a prime number, return "YES",
    // otherwise, return "NO".
    // If the two intervals don't intersect, return "NO".
    // [input/output] samples:
    // >>> intersection((Pair.with(1l, 2l)), (Pair.with(2l, 3l)))
    // ("NO")
    // >>> intersection((Pair.with(-1l, 1l)), (Pair.with(0l, 4l)))
    // ("NO")
    // >>> intersection((Pair.with(-3l, -1l)), (Pair.with(-5l, 5l)))
    // ("YES")
    public static String intersection(Pair<Long, Long> interval1, Pair<Long, Long> interval2) {

        // Check if the two intervals are intersecting
        // if (condition)
        if (interval1.getValue0() >= interval2.getValue1() || interval1.getValue1() <= interval2.getValue0()) {
            return "NO";
        }
        // Find the intersection
        // (long) (Math.max(interval1.getValue0(), interval2.getValue0()))
        long intersectionStart = Math.max(interval1.getValue0(), interval2.getValue0());
        // (long) (Math.min(interval1.getValue1(), interval2.getValue1()))
        long intersectionEnd = Math.min(interval1.getValue1(), interval2.getValue1());
        // Find the length of the intersection
        long intersectionLength = intersectionEnd - intersectionStart + 1l;
        // Check if the length is a prime number
        // if (condition)
        if (isPrime(intersectionLength)) {
            return "YES";
        } else {
            return "NO";
        }
    }
    public static void main(String[] args) {
    assert(intersection((Pair.with(1l, 2l)), (Pair.with(2l, 3l))).equals(("NO")));
    assert(intersection((Pair.with(-1l, 1l)), (Pair.with(0l, 4l))).equals(("NO")));
    assert(intersection((Pair.with(-3l, -1l)), (Pair.with(-5l, 5l))).equals(("YES")));
    assert(intersection((Pair.with(-2l, 2l)), (Pair.with(-4l, 0l))).equals(("YES")));
    assert(intersection((Pair.with(-11l, 2l)), (Pair.with(-1l, -1l))).equals(("NO")));
    assert(intersection((Pair.with(1l, 2l)), (Pair.with(3l, 5l))).equals(("NO")));
    assert(intersection((Pair.with(1l, 2l)), (Pair.with(1l, 2l))).equals(("NO")));
    assert(intersection((Pair.with(-2l, -2l)), (Pair.with(-3l, -2l))).equals(("NO")));
    }

}
