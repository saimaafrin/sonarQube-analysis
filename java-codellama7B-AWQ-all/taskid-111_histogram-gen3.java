import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string representing a space separated lowercase letters, return a hash map
    // of the letter with the most repetition and containing the corresponding count.
    // If several letters have the same occurrence, return all of them.
    // Example:
    // >>> histogram(("a b c"))
    // (new HashMap<String,Long>(Map.of("a", 1l, "b", 1l, "c", 1l)))
    // >>> histogram(("a b b a"))
    // (new HashMap<String,Long>(Map.of("a", 2l, "b", 2l)))
    // >>> histogram(("a b c a b"))
    // (new HashMap<String,Long>(Map.of("a", 2l, "b", 2l)))
    // >>> histogram(("b b b b a"))
    // (new HashMap<String,Long>(Map.of("b", 4l)))
    // >>> histogram((""))
    // (new HashMap<String,Long>())
    public static HashMap<String,Long> histogram(String test) {

        // Initialize the hash map and count the number of repetitions.
        HashMap<String,Long> hashMap = new HashMap<String,Long>();
        long maxCount = 0;
        String letter = "";
        for (int i=0; i<test.length(); i++) {
            String currentLetter = String.valueOf(test.charAt(i));
            if (hashMap.containsKey(currentLetter)) {
                hashMap.put(currentLetter, hashMap.get(currentLetter) + 1);
                if (hashMap.get(currentLetter) > maxCount) {
                    maxCount = hashMap.get(currentLetter);
                    letter = currentLetter;
                }
            } else {
                hashMap.put(currentLetter, 1L);
                if (hashMap.get(currentLetter) > maxCount) {
                    maxCount = hashMap.get(currentLetter);
                    letter = currentLetter;
                }
            }
        }
        // Return the resulting hash map.
        if (letter.equals("")) {
            return new HashMap<String,Long>();
        } else {
            return new HashMap<String,Long>(Map.of(letter, maxCount));
        }
    }
    public static void main(String[] args) {
    assert(histogram(("a b b a")).equals((new HashMap<String,Long>(Map.of("a", 2l, "b", 2l)))));
    assert(histogram(("a b c a b")).equals((new HashMap<String,Long>(Map.of("a", 2l, "b", 2l)))));
    assert(histogram(("a b c d g")).equals((new HashMap<String,Long>(Map.of("a", 1l, "b", 1l, "c", 1l, "d", 1l, "g", 1l)))));
    assert(histogram(("r t g")).equals((new HashMap<String,Long>(Map.of("r", 1l, "t", 1l, "g", 1l)))));
    assert(histogram(("b b b b a")).equals((new HashMap<String,Long>(Map.of("b", 4l)))));
    assert(histogram(("r t g")).equals((new HashMap<String,Long>(Map.of("r", 1l, "t", 1l, "g", 1l)))));
    assert(histogram(("")).equals((new HashMap<String,Long>())));
    assert(histogram(("a")).equals((new HashMap<String,Long>(Map.of("a", 1l)))));
    }

}
