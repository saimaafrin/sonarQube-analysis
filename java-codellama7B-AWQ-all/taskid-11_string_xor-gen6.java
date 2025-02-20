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

        // Check if there is an easy solution without converting to binary and back.
        if (a.length() != b.length()) {
            // Can't perform XOR if lengths differ.
            return null;
        }
        if (a.isEmpty()) {
            // Can't perform XOR if either string is empty.
            return null;
        }
        if (a.equals(b)) {
            // If strings are equal, XOR is also an empty string.
            return "";
        }
        // Convert both to binary numbers and perform XOR on them.
        BigInteger biA = new BigInteger(a, 2);
        BigInteger biB = new BigInteger(b, 2);
        BigInteger result = biA.xor(biB);
        return result.toString(2);
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
