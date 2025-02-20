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

        long mod = 10l;
        long modpow = 1l;
        while (mod <= x) {
            mod *= 10;
            modpow *= 10;
        }
        long nx = x / mod;
        long rx = x % mod;
        long rxNew = rx * modpow;
        long nxNew = nx + rxNew;
        StringBuilder sb = new StringBuilder(Long.toString(nxNew));
        if (shift < sb.length()) {
            sb.delete(0, sb.length() - shift);
        } else {
            shift -= sb.length();
            while (shift > 0) {
                sb.append(sb.deleteCharAt(0));
                shift--;
            }
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
