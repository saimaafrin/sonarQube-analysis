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

        String s = String.valueOf(x);
        if (shift >= s.length()) {
            char[] reversed = s.toCharArray();
            Arrays.sort(reversed);
            return new String(reversed);
        }
        // Circularly shift an array of n elements
        int n = s.length()-1;
        for (int i=0; i<shift; i++) {
            char temp = s.charAt(0);
            for (int j=0; j<n; j++) {
                s = s.substring(1) + temp;
            }
        }
        return s;
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
