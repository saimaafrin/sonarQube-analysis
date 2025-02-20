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

        String str = Long.toString(x);
        char[] arr = new char[str.length()];
        for (int i = 0; i < str.length(); i++) {
            arr[i] = str.charAt(i);
        }
        int len = str.length();
        if (shift >= len) {
            for (int i = 0; i < shift; i++) {
                int index = arr.length - 1;
                char temp = arr[index];
                for (int j = index; j > 0; j--) {
                    arr[j] = arr[j - 1];
                }
                arr[0] = temp;
            }
        }
        else {
            for (int i = 0; i < shift; i++) {
                int index = arr.length - 1;
                char temp = arr[index];
                for (int j = index; j > 0; j--) {
                    arr[j] = arr[j - 1];
                }
                arr[0] = temp;
            }
        }
        return new String(arr);
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
