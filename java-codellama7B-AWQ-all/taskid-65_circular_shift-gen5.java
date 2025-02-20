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

        String result = Long.toString(x);
        if(shift <= result.length()) {
            result = result.substring(shift, result.length()) + result.substring(0, shift);
        } else {
            String temp = Long.toString(x);
            int count = 0;
            String temp2 = "";
            while(temp.length() != 0) {
                temp2 += temp.substring(1, temp.length());
                temp = temp.substring(0, temp.length() - 1);
                count++;
            }
            result = temp2 + result.substring(0, shift - count);
        }
        return result;
    }
    public static void main(String[] args) {
    assert(circularShift((100l), (2l)).equals(("001")));
    assert(circularShift((12l), (2l)).equals(("12")));
    assert(circularShift((97l), (8l)).equals(("79")));
    assert(circularShift((12l), (1l)).equals(("21")));
    assert(circularShift((11l), (101l)).equals(("11")));
    }

}
