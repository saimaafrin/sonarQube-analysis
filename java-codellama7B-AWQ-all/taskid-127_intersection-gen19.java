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

        if (interval1.getValue0() > interval1.getValue1() || interval2.getValue0() > interval2.getValue1()) {
            return "NO";
        }
        if ((interval1.getValue0() >= interval2.getValue1()) || (interval2.getValue0() >= interval1.getValue1())) {
            return "NO";
        }
        long intersectionStart = Math.max(interval1.getValue0(), interval2.getValue0());
        long intersectionEnd = Math.min(interval1.getValue1(), interval2.getValue1());
        long intersectionLength = intersectionEnd - intersectionStart + 1;
        if (intersectionLength < 0) {
            return "NO";
        }
        if (intersectionLength == 0) {
            return "NO";
        }
        if (intersectionLength == 1) {
            return "NO";
        }
        long isPrime = 0;
        for (long i = 1; i <= intersectionLength; i++) {
            if (intersectionLength % i == 0) {
                isPrime++;
            }
        }
        if (isPrime > 1) {
            return "NO";
        } else {
            return "YES";
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
