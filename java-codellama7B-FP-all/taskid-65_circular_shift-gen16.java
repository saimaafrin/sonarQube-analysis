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

        // Create a string of the digits
        String digits = Long.toString(x);
        // If we shift more than the number of digits, reverse the string
        if (shift > digits.length()) {
            shift = digits.length();
        }
        // Use substring to get the end of the string
        String end = digits.substring(digits.length() - shift, digits.length());
        // Use substring to get the start of the string
        String start = digits.substring(0, digits.length() - shift);
        // Reverse the digits and append them
        return start + new StringBuilder(end).reverse().toString();
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
