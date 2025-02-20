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

        // (1)
        long count = 0;
        for (int i = 0; i <= string.length() - substring.length(); i++) {
            // (2)
            boolean match = true;
            for (int j = 0; j < substring.length(); j++) {
                // (3)
                if (string.charAt(i + j) != substring.charAt(j)) {
                    match = false;
                }
            }
            // (4)
            if (match) {
                count++;
            }
        }
        // (5)
        return count;
    }
    public static void main(String[] args) {
    assert(howManyTimes((""), ("x")) == (0l));
    assert(howManyTimes(("xyxyxyx"), ("x")) == (4l));
    assert(howManyTimes(("cacacacac"), ("cac")) == (4l));
    assert(howManyTimes(("john doe"), ("john")) == (1l));
    }

}
