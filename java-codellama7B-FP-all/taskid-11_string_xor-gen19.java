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

        StringBuilder result = new StringBuilder(Math.max(a.length(), b.length()));
        for (int i = 0, j = 0; i < a.length() || j < b.length(); i++, j++) {
            if (i < a.length()) {
                if (j < b.length()) {
                    char ch = (a.charAt(i) == b.charAt(j)) ? '0' : '1';
                    result.append(ch);
                } else {
                    result.append(a.charAt(i));
                }
            } else {
                result.append(b.charAt(j));
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
