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

        // String s = "" + x;
        String s = Long.toString(x);
        int l = s.length();
        if (l < shift) {
            return new StringBuilder(s).reverse().toString();
        }
        if (l == shift) {
            return new StringBuilder(s).reverse().toString();
        }
        StringBuilder sb = new StringBuilder();
        int i = shift;
        while (i < l) {
            sb.append(s.charAt(i));
            i++;
        }
        i = 0;
        while (i < shift) {
            sb.append(s.charAt(i));
            i++;
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
