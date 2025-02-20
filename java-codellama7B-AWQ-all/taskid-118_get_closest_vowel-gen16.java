import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a word. Your task is to find the closest vowel that stands between 
    // two consonants from the right side of the word (case sensitive).
    // Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    // find any vowel met the above condition. 
    // You may assume that the given string contains English letter only.
    // Example:
    // >>> getClosestVowel(("yogurt"))
    // ("u")
    // >>> getClosestVowel(("FULL"))
    // ("U")
    // >>> getClosestVowel(("quick"))
    // ("")
    // >>> getClosestVowel(("ab"))
    // ("")
    public static String getClosestVowel(String word) {

        // Write your code here
        if(word.length() < 2) {
            return "";
        }
        int i = 0;
        while(i < word.length() && !Character.isLetter(word.charAt(i))) {
            i++;
        }
        if(i == word.length()) {
            return "";
        }
        while(i < word.length() && !Character.isUpperCase(word.charAt(i))) {
            i++;
        }
        if(i == word.length()) {
            return "";
        }
        int start = i;
        while(i < word.length() && Character.isUpperCase(word.charAt(i))) {
            i++;
        }
        if(i == word.length()) {
            return "";
        }
        while(i < word.length() && !Character.isLetter(word.charAt(i))) {
            i++;
        }
        if(i == word.length()) {
            return "";
        }
        int end = i;
        if(start == end) {
            return "";
        }
        return word.substring(start, end);
    }
    public static void main(String[] args) {
    assert(getClosestVowel(("yogurt")).equals(("u")));
    assert(getClosestVowel(("full")).equals(("u")));
    assert(getClosestVowel(("easy")).equals(("")));
    assert(getClosestVowel(("eAsy")).equals(("")));
    assert(getClosestVowel(("ali")).equals(("")));
    assert(getClosestVowel(("bad")).equals(("a")));
    assert(getClosestVowel(("most")).equals(("o")));
    assert(getClosestVowel(("ab")).equals(("")));
    assert(getClosestVowel(("ba")).equals(("")));
    assert(getClosestVowel(("quick")).equals(("")));
    assert(getClosestVowel(("anime")).equals(("i")));
    assert(getClosestVowel(("Asia")).equals(("")));
    assert(getClosestVowel(("Above")).equals(("o")));
    }

}
