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

        // String string = "abcdefg";
        // String substring = "def";
        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            int j = i;
            int k = 0;
            while (k < substring.length()) {
                if (j == string.length()) {
                    break;
                }
                if (substring.charAt(k) == string.charAt(j)) {
                    k++;
                    j++;
                } else {
                    j++;
                }
            }
            if (k == substring.length()) {
                count++;
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
