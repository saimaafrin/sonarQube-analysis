import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Out of array list of strings, return the longest one. Return the first one in case of multiple
    // strings of the same length. Return null in case the input array list is empty.
    // >>> longest((new ArrayList<String>(Arrays.asList())))
    // Optional.empty()
    // >>> longest((new ArrayList<String>(Arrays.asList((String)"a", (String)"b", (String)"c"))))
    // "a"
    // >>> longest((new ArrayList<String>(Arrays.asList((String)"a", (String)"bb", (String)"ccc"))))
    // "ccc"
    public static Optional<String> longest(ArrayList<String> strings) {

        if(strings.size() == 0) {
            return Optional.empty();
        }
        String longest = strings.get(0);
        for(String s : strings) {
            if(s.length() > longest.length()) {
                longest = s;
            } else if(s.length() == longest.length() && s.compareTo(longest) < 0) {
                longest = s;
            }
        }
        return Optional.of(longest);
    }
    public static void main(String[] args) {
    assert(longest((new ArrayList<String>(Arrays.asList()))).equals(Optional.empty()));
    assert(longest((new ArrayList<String>(Arrays.asList((String)"x", (String)"y", (String)"z")))).equals("x"));
    assert(longest((new ArrayList<String>(Arrays.asList((String)"x", (String)"yyy", (String)"zzzz", (String)"www", (String)"kkkk", (String)"abc")))).equals("zzzz"));
    }

}
