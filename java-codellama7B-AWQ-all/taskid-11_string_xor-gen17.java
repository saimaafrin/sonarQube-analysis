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

        if (a.length() != b.length()) {
            throw new IllegalArgumentException("Inputs must be of same length");
        }
        char[] result = new char[a.length()];
        for (int i = 0; i < a.length(); ++i) {
            result[i] = Character.forDigit(Integer.bitCount(Integer.parseInt(a.substring(i, i + 1)) ^ Integer.parseInt(b.substring(i, i + 1))), 10);
        }
        return new String(result);
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
