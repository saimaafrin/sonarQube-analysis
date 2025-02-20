import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input are two strings a and b consisting only of 1s and 0s.
    // Perform binary XOR on these inputs and return result also as a string.
    // >>> stringXor(("010"), ("110"))
    // ("100")
    public static String stringXor(String a, String b) {

        int na = a.length(), nb = b.length();
        int n = Math.max(na, nb);
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            if (i < na) {
                char ch = a.charAt(i);
                if (ch == '1') {
                    sb.append('1');
                } else {
                    sb.append('0');
                }
            } else {
                sb.append('0');
            }
            if (i < nb) {
                char ch = b.charAt(i);
                if (ch == '1') {
                    sb.append('1');
                } else {
                    sb.append('0');
                }
            } else {
                sb.append('0');
            }
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
