import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function that takes a value (string) representing a number
    // and returns the closest integer to it. If the number is equidistant
    // from two integers, round it away from zero.
    // Examples
    // >>> closestInteger(("10"))
    // (10l)
    // >>> closestInteger(("15.3"))
    // (15l)
    // Note:
    // Rounding away from zero means that if the given number is equidistant
    // from two integers, the one you should return is the one that is the
    // farthest from zero. For example closest_integer("14.5") should
    // return 15 and closest_integer("-14.5") should return -15.
    public static long closestInteger(String value) {

        // Your code here.
        long ret = 0;
        long min = Long.MAX_VALUE;
        long max = Long.MIN_VALUE;
        long x = 0;
        try {
            x = Long.valueOf(value);
        } catch (NumberFormatException ex) {
            return ret;
        }
        long lower = x - 1;
        long upper = x + 1;
        for (long i = 0; i <= upper; i++) {
            long abs = Math.abs(i);
            if (abs < min) {
                min = abs;
                ret = i;
            }
        }
        for (long i = lower; i <= upper; i++) {
            long abs = Math.abs(i);
            if (abs > max) {
                max = abs;
                ret = i;
            }
        }
        return ret;
    }
    public static void main(String[] args) {
    assert(closestInteger(("10")) == (10l));
    assert(closestInteger(("14.5")) == (15l));
    assert(closestInteger(("-15.5")) == (-16l));
    assert(closestInteger(("15.3")) == (15l));
    assert(closestInteger(("0")) == (0l));
    }

}
