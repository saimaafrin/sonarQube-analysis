import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string, find out how many distinct characters (regardless of case) does it consist of
    // >>> countDistinctCharacters(("xyzXYZ"))
    // (3l)
    // >>> countDistinctCharacters(("Jerry"))
    // (4l)
    public static long countDistinctCharacters(String string) {

        // Create a map to hold unique characters. The map will help us to avoid duplicate characters in the output.
        Map<String, Long> map = new HashMap<>();
        // Get all lowercase characters.
        String lower = string.toLowerCase();
        // Go over all characters and increment their count in the map.
        for (int i = 0; i < lower.length(); i++) {
            String currentChar = lower.charAt(i) + "";
            if (map.containsKey(currentChar)) {
                map.put(currentChar, map.get(currentChar) + 1L);
            } else {
                map.put(currentChar, 1L);
            }
        }
        // Get the total count of unique characters.
        long count = 0L;
        for (String key : map.keySet()) {
            count += map.get(key);
        }
        return count;
    }
    public static void main(String[] args) {
    assert(countDistinctCharacters(("")) == (0l));
    assert(countDistinctCharacters(("abcde")) == (5l));
    assert(countDistinctCharacters(("abcdecadeCADE")) == (5l));
    assert(countDistinctCharacters(("aaaaAAAAaaaa")) == (1l));
    assert(countDistinctCharacters(("Jerry jERRY JeRRRY")) == (5l));
    }

}
