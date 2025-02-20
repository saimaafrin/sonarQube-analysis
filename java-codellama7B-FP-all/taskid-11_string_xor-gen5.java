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
        int c = 0;
        for (int i = 0; i < a.length(); i++) {
            if ((a.charAt(i) == '1') != (b.charAt(i) == '1')) {
                c = c + 1;
            }
        }
        for (int i = 0; i < a.length(); i++) {
            if ((a.charAt(i) == '1') == (b.charAt(i) == '1')) {
                result = result + "0";
            } else {
                result = result + "1";
            }
        }
        if (c % 2 == 0) {
            result = result + "0";
        } else {
            result = result + "1";
        }
        return result;
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
