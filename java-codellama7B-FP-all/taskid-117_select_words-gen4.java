import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string s and a natural number n, you have been tasked to implement 
    // a function that returns an array array list of all words from string s that contain exactly 
    // n consonants, in order these words appear in the string s.
    // If the string s is empty then the function should return an empty array list.
    // Note: you may assume the input string contains only letters and spaces.
    // Examples:
    // >>> selectWords(("Mary had a little lamb"), (4l))
    // (new ArrayList<String>(Arrays.asList((String)"little")))
    // >>> selectWords(("Mary had a little lamb"), (3l))
    // (new ArrayList<String>(Arrays.asList((String)"Mary", (String)"lamb")))
    // >>> selectWords(("simple white space"), (2l))
    // (new ArrayList<String>(Arrays.asList()))
    // >>> selectWords(("Hello world"), (4l))
    // (new ArrayList<String>(Arrays.asList((String)"world")))
    // >>> selectWords(("Uncle sam"), (3l))
    // (new ArrayList<String>(Arrays.asList((String)"Uncle")))
    public static ArrayList<String> selectWords(String s, long n) {

        // The solution has to be in-place, using only the input parameter s and n.
        // No global variables, no instance variables, no static variables, no external
        // variables or objects.
        // Also, don't use any helper functions.
        // The time complexity of your solution has to be O(n) where n is the length of the string s.
        // The space complexity of your solution has to be O(n) where n is the length of the string s.
        ArrayList<String> output = new ArrayList<String>();
        if (s.length() == 0 || n <= 0)
            return output;
        // 1. Find all words in s.
        String[] words = s.split(" ");
        // 2. For each word, count its consonants.
        int len = words.length;
        int count = 0;
        for (int i = 0; i < len; i++) {
            String word = words[i];
            if (word.length() == 0)
                continue;
            count = 0;
            for (int j = 0; j < word.length(); j++) {
                char ch = word.charAt(j);
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'y')
                    continue;
                count++;
            }
            // 3. If the word has exactly n consonants, add it to output.
            if (count == n)
                output.add(word);
        }
        return output;
    }
    public static void main(String[] args) {
    assert(selectWords(("Mary had a little lamb"), (4l)).equals((new ArrayList<String>(Arrays.asList((String)"little")))));
    assert(selectWords(("Mary had a little lamb"), (3l)).equals((new ArrayList<String>(Arrays.asList((String)"Mary", (String)"lamb")))));
    assert(selectWords(("simple white space"), (2l)).equals((new ArrayList<String>(Arrays.asList()))));
    assert(selectWords(("Hello world"), (4l)).equals((new ArrayList<String>(Arrays.asList((String)"world")))));
    assert(selectWords(("Uncle sam"), (3l)).equals((new ArrayList<String>(Arrays.asList((String)"Uncle")))));
    assert(selectWords((""), (4l)).equals((new ArrayList<String>(Arrays.asList()))));
    assert(selectWords(("a b c d e f"), (1l)).equals((new ArrayList<String>(Arrays.asList((String)"b", (String)"c", (String)"d", (String)"f")))));
    }

}
