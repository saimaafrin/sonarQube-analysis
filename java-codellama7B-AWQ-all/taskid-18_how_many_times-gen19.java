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

        long count = 0;
        if (string.isEmpty() || substring.isEmpty()) return count;

        int sublen = substring.length();

        // Start the search from the beginning of the string.
        for (int i = 0; i <= (string.length() - sublen); i++) {
            // Check for a match at the current index.
            if (string.substring(i, i + sublen).equals(substring)) {
                count++;
                // Check if there is an overlap between the two strings.
                // (e.g. string = "aaa" and substring = "aa")
                if (i < (string.length() - sublen)) {
                    // If there is an overlap, search again from there.
                    i += sublen;
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
    assert(howManyTimes((""), ("x")) == (0l));
    assert(howManyTimes(("xyxyxyx"), ("x")) == (4l));
    assert(howManyTimes(("cacacacac"), ("cac")) == (4l));
    assert(howManyTimes(("john doe"), ("john")) == (1l));
    }

}
