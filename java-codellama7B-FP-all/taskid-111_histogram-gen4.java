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

        if (test.equals("")) {
            return new HashMap<String,Long>();
        }
        String[] words = test.split(" ");
        HashMap<String, Long> hist = new HashMap<String, Long>();
        for (String word: words) {
            if (hist.containsKey(word)) {
                hist.put(word, hist.get(word) + 1);
            }
            else {
                hist.put(word, 1L);
            }
        }
        for (String key : hist.keySet()) {
            if (hist.get(key) == Collections.max(hist.values())) {
                hist = new HashMap<String, Long>(Map.of(key, hist.get(key)));
                break;
            }
        }
        return hist;
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
