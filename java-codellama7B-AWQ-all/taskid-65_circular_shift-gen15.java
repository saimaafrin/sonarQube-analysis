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

        // The string representation of x
        String xs = Long.toString(x);
        // The length of the string representation of x
        int xl = xs.length();
        // The shifted string
        String ys;
        // The final string to return
        String zs;
        // If the shift is less than the length
        if (shift < xl) {
            // Shift the string
            ys = xs.substring(shift) + xs.substring(0, shift);
        }
        // If the shift is greater than the length
        else {
            // Shift the string
            ys = xs.substring(0, shift - xl) + xs.substring(xl - shift);
        }
        // The string to return
        zs = ys;
        // Return the shifted string
        return zs;
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
