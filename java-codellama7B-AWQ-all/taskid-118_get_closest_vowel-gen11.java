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

        String[] vowels = {"a", "e", "i", "o", "u"};
        if(word.length() < 2) return "";
        char[] charArray = word.toCharArray();
        char firstChar = charArray[0];
        char lastChar = charArray[word.length() - 1];
        String firstCharStr = String.valueOf(firstChar);
        String lastCharStr = String.valueOf(lastChar);
        if(Arrays.asList(vowels).contains(firstCharStr))
        {
            if(Arrays.asList(vowels).contains(lastCharStr))
            {
                return "";
            }
            else
            {
                return lastCharStr;
            }
        }
        else if(Arrays.asList(vowels).contains(lastCharStr))
        {
            return firstCharStr;
        }
        else
        {
            for(int i = 1; i < word.length() - 1; i++)
            {
                if(Arrays.asList(vowels).contains(String.valueOf(word.charAt(i))))
                {
                    return String.valueOf(word.charAt(i));
                }
            }
            return "";
        }
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
