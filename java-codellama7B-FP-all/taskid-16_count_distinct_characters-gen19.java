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

        // Initialize a hash map of the characters in the string
        HashMap<String, Boolean> hashMap = new HashMap<>();
        for (int i = 0; i < string.length(); i++) {
            // Hash the string in lowercase
            String hashedString = String.valueOf(string.charAt(i)).toLowerCase();
            // Check if the hashed string is already in the hash map
            if (!hashMap.containsKey(hashedString)) {
                // If it is not, add it to the hash map
                hashMap.put(hashedString, true);
            }
        }
        // Return the number of elements in the hash map
        return hashMap.size();
    }
    public static void main(String[] args) {
    assert(countDistinctCharacters(("")) == (0l));
    assert(countDistinctCharacters(("abcde")) == (5l));
    assert(countDistinctCharacters(("abcdecadeCADE")) == (5l));
    assert(countDistinctCharacters(("aaaaAAAAaaaa")) == (1l));
    assert(countDistinctCharacters(("Jerry jERRY JeRRRY")) == (5l));
    }

}
