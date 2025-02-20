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

        if (shift > x.toString().length()) {
            return new StringBuilder(x.toString()).reverse().toString();
        }
        StringBuilder s = new StringBuilder(x.toString());
        char[] charArray = s.toString().toCharArray();
        int length = charArray.length;
        int index = 0;
        if (shift == length) {
            return new StringBuilder(x.toString()).reverse().toString();
        }
        char[] shiftedCharArray = new char[length];
        for (int i = 0; i < length - shift; i++) {
            shiftedCharArray[i] = charArray[i + shift];
        }
        for (int i = length - shift; i < length; i++) {
            shiftedCharArray[i] = charArray[i - (length - shift)];
        }
        return new StringBuilder(new String(shiftedCharArray)).reverse().toString();
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
