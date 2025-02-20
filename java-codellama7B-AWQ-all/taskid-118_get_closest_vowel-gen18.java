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

        // you can write to stdout for debugging purposes, e.g.
        // System.out.println("this is a debug message");
        int i = word.length();
        int j = 0;
        while(i > 0 && j < word.length()) {
            if (Character.isLetter(word.charAt(i)) && Character.isLetter(word.charAt(j))) {
                if (Character.isUpperCase(word.charAt(i))) {
                    i--;
                } else if (Character.isUpperCase(word.charAt(j))) {
                    j++;
                } else {
                    break;
                }
            } else {
                if (Character.isUpperCase(word.charAt(i))) {
                    i--;
                } else if (Character.isUpperCase(word.charAt(j))) {
                    j++;
                } else {
                    i--;
                    j++;
                }
            }
        }
        if (Character.isUpperCase(word.charAt(i))) {
            return "";
        }
        while(i > 0) {
            if (Character.isLetter(word.charAt(i))) {
                if (Character.isLowerCase(word.charAt(i))) {
                    return word.charAt(i)+"";
                }
            }
            i--;
        }
        return "";
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
