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

        ArrayList<String> result = new ArrayList<>();
        if (s.isEmpty()) {
            return result;
        }
        // Find start and end index of first word
        int start = 0;
        while (start < s.length() && !Character.isLetter(s.charAt(start))) {
            start++;
        }
        // Find end index of last word
        int end = s.length() - 1;
        while (end >= 0 && !Character.isLetter(s.charAt(end))) {
            end--;
        }
        // Iterate through each word and check if it has n consonants
        for (int i = start; i <= end; i++) {
            // Find start and end index of word
            int wordStart = i;
            while (wordStart <= end && !Character.isLetter(s.charAt(wordStart))) {
                wordStart++;
            }
            int wordEnd = i;
            while (wordEnd <= end && Character.isLetter(s.charAt(wordEnd))) {
                wordEnd++;
            }
            // Check if word has n consonants
            int consonants = 0;
            for (int j = wordStart; j < wordEnd; j++) {
                if (!Character.isLetter(s.charAt(j))) {
                    consonants++;
                }
            }
            if (consonants == n) {
                result.add(s.substring(wordStart, wordEnd));
            }
        }
        return result;
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
