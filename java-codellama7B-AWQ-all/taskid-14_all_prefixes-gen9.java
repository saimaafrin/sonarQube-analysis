import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return array list of all prefixes from shortest to longest of the input string
    // >>> allPrefixes(("abc"))
    // (new ArrayList<String>(Arrays.asList((String)"a", (String)"ab", (String)"abc")))
    public static ArrayList<String> allPrefixes(String string) {

        // Start with an empty prefix
        String prefix = "";
        // Start with an empty list of prefixes
        ArrayList<String> prefixes = new ArrayList<>();
        // Loop through each character in the input string
        for (int i = 0; i < string.length(); i++) {
            // Add the current character to the prefix
            prefix = prefix + string.charAt(i);
            // Add the current prefix to the list of prefixes
            prefixes.add(prefix);
        }
        // Return the list of prefixes
        return prefixes;
    }
    public static void main(String[] args) {
    assert(allPrefixes(("")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(allPrefixes(("asdfgh")).equals((new ArrayList<String>(Arrays.asList((String)"a", (String)"as", (String)"asd", (String)"asdf", (String)"asdfg", (String)"asdfgh")))));
    assert(allPrefixes(("WWW")).equals((new ArrayList<String>(Arrays.asList((String)"W", (String)"WW", (String)"WWW")))));
    }

}
