import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Circular shift the digits of the integer x, shift the digits right by shift
    // and return the result as a string.
    // If shift > number of digits, return digits reversed.
    // >>> circularShift((12l), (1l))
    // ("21")
    // >>> circularShift((12l), (2l))
    // ("12")
    public static String circularShift(long x, long shift) {

        final String num = String.valueOf(x);
        final int len = num.length();
        int digits = (int) Math.min(shift, len);
        int start = len - digits;
        int end = start + digits;
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < start; ++i) {
            result.append(num.charAt(i));
        }
        for (int i = end; i < len; ++i) {
            result.append(num.charAt(i));
        }
        for (int i = start; i < end; ++i) {
            result.append(num.charAt(i));
        }
        return result.toString();
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
