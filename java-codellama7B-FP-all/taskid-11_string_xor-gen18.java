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

        String result = "";
        int i = 0;
        while (i < a.length() && i < b.length()) {
            int xor = 0;
            if (a.charAt(i) == '1') xor += 1;
            if (b.charAt(i) == '1') xor += 2;
            result = (xor == 0 ? "0" : "1") + result;
            i++;
        }
        while (i < a.length()) {
            int xor = 0;
            if (a.charAt(i) == '1') xor += 1;
            result = (xor == 0 ? "0" : "1") + result;
            i++;
        }
        while (i < b.length()) {
            int xor = 0;
            if (b.charAt(i) == '1') xor += 2;
            result = (xor == 0 ? "0" : "1") + result;
            i++;
        }
        return result;
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
