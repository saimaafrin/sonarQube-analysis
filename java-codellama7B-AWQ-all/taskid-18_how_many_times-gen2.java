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

        if (string.length() == 0) {
            return 0;
        }
        if (substring.length() == 0) {
            return 0;
        }
        if (substring.length() > string.length()) {
            return 0;
        }
        long counter = 0;
        int j = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == substring.charAt(j)) {
                j++;
                if (j == substring.length()) {
                    counter++;
                    j = 0;
                }
            }
            else {
                j = 0;
            }
        }
        return counter;
    }
    public static void main(String[] args) {
    assert(howManyTimes((""), ("x")) == (0l));
    assert(howManyTimes(("xyxyxyx"), ("x")) == (4l));
    assert(howManyTimes(("cacacacac"), ("cac")) == (4l));
    assert(howManyTimes(("john doe"), ("john")) == (1l));
    }

}
