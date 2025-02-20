import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Find how many times a given substring can be found in the original string. Count overlaping cases.
    // >>> howManyTimes((""), ("a"))
    // (0l)
    // >>> howManyTimes(("aaa"), ("a"))
    // (3l)
    // >>> howManyTimes(("aaaa"), ("aa"))
    // (3l)
    public static long howManyTimes(String string, String substring) {

        long result = 0;
        int stringLength = string.length();
        int substringLength = substring.length();
        if (stringLength == 0) {
            return result;
        }
        if (substringLength == 0) {
            return 0;
        }
        if (stringLength < substringLength) {
            return 0;
        }
        for (int i = 0; i < stringLength; i++) {
            if (string.substring(i, i + substringLength).equals(substring)) {
                result++;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(howManyTimes((""), ("x")) == (0l));
    assert(howManyTimes(("xyxyxyx"), ("x")) == (4l));
    assert(howManyTimes(("cacacacac"), ("cac")) == (4l));
    assert(howManyTimes(("john doe"), ("john")) == (1l));
    }

}
