import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string s, count the number of uppercase vowels in even indices.
    // For example:
    // >>> countUpper(("aBCdEf"))
    // (1l)
    // >>> countUpper(("abcdefg"))
    // (0l)
    // >>> countUpper(("dBBE"))
    // (0l)
    public static long countUpper(String s) {

        long count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            if (s.charAt(i) == 'A' || s.charAt(i) == 'E' || s.charAt(i) == 'I' || s.charAt(i) == 'O' || s.charAt(i) == 'U') {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
    assert(countUpper(("aBCdEf")) == (1l));
    assert(countUpper(("abcdefg")) == (0l));
    assert(countUpper(("dBBE")) == (0l));
    assert(countUpper(("B")) == (0l));
    assert(countUpper(("U")) == (1l));
    assert(countUpper(("")) == (0l));
    assert(countUpper(("EEEE")) == (2l));
    }

}
