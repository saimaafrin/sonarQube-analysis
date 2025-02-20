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

        // The answer we will return
        long answer = 0l;

        // Loop through the string
        for (int i = 0; i < s.length(); i++) {
            // Check if the character is an uppercase vowel
            if (Character.toUpperCase(s.charAt(i)) == 'A' || Character.toUpperCase(s.charAt(i)) == 'E' || Character.toUpperCase(s.charAt(i)) == 'I' || Character.toUpperCase(s.charAt(i)) == 'O' || Character.toUpperCase(s.charAt(i)) == 'U') {
                // If it is, increment the answer
                if (i % 2 == 0) {
                    answer += 1;
                }
            }
        }
        // Return the answer
        return answer;
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
