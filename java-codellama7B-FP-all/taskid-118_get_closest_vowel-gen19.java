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

        int i=0;
        int j=word.length()-1;
        while(i<j){
            if(word.charAt(i)==word.charAt(j)){
                i++;
                j--;
            }else{
                if(isVowel(word.charAt(i)) && !isVowel(word.charAt(j))){
                    j--;
                }else{
                    if(!isVowel(word.charAt(i)) && isVowel(word.charAt(j))){
                        i++;
                    }else{
                        if(!isVowel(word.charAt(i)) && !isVowel(word.charAt(j))){
                            i++;
                            j--;
                        }else{
                            break;
                        }
                    }
                }
            }
        }
        if(i>=j)return "";
        if(isVowel(word.charAt(i))){
            return ""+word.charAt(i);
        }else{
            return ""+word.charAt(j);
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
