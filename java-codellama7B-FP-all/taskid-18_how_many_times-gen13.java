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

        // (0l)
        if (string.length() == 0) return 0;
        // (0l)
        if (substring.length() == 0) return 0;
        // (0l)
        if (string.length() < substring.length()) return 0;
        // (0l)
        if (string.equals(substring)) return 1;
        long result = 0;
        for (int i = 0; i < string.length(); i++) {
            result += howManyTimes(string.substring(i), substring);
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
