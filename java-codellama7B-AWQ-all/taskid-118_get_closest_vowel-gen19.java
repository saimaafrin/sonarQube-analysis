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

        int[] vowels = new int[] { word.indexOf('a'), word.indexOf('e'), word.indexOf('i'), word.indexOf('o'), word.indexOf('u') };
        int[] consonants = new int[] { word.lastIndexOf('b'), word.lastIndexOf('c'), word.lastIndexOf('d'), word.lastIndexOf('f'), word.lastIndexOf('g'), word.lastIndexOf('h'), word.lastIndexOf('j'), word.lastIndexOf('k'), word.lastIndexOf('l'), word.lastIndexOf('m'), word.lastIndexOf('n'), word.lastIndexOf('p'), word.lastIndexOf('q'), word.lastIndexOf('r'), word.lastIndexOf('s'), word.lastIndexOf('t'), word.lastIndexOf('v'), word.lastIndexOf('w'), word.lastIndexOf('x'), word.lastIndexOf('y'), word.lastIndexOf('z') };
        Arrays.sort(consonants);
        Arrays.sort(vowels);
        for (int i = vowels.length - 1; i >= 0; i--) {
            for (int j = consonants.length - 1; j >= 0; j--) {
                if (consonants[j] > vowels[i]) {
                    return word.substring(vowels[i] + 1, consonants[j]);
                }
            }
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
