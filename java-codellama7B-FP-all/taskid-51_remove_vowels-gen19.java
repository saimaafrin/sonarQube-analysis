import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // remove_vowels is a function that takes string and returns string without vowels.
    // >>> removeVowels((""))
    // ("")
    // >>> removeVowels(("abcdef"))
    // ("bcdf")
    // >>> removeVowels(("aaaaa"))
    // ("")
    // >>> removeVowels(("aaBAA"))
    // ("B")
    // >>> removeVowels(("zbcd"))
    // ("zbcd")
    public static String removeVowels(String text) {

        // *** YOUR CODE HERE ***
        // IMPORTANT:
        // You should not modify the given text string.
        // Instead, make a new string without vowels.
        // If there are no vowels in the given text, return the given text.
        char[] arr = text.toCharArray();
        String noVowels = new String();
        for(char c : arr){
            if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u'){
                noVowels += c;
            }
        }
        if(noVowels.equals("")){
            return text;
        }
        return noVowels;
    }
    public static void main(String[] args) {
    assert(removeVowels(("")).equals(("")));
    assert(removeVowels(("abcdef\nghijklm")).equals(("bcdf\nghjklm")));
    assert(removeVowels(("fedcba")).equals(("fdcb")));
    assert(removeVowels(("eeeee")).equals(("")));
    assert(removeVowels(("acBAA")).equals(("cB")));
    assert(removeVowels(("EcBOO")).equals(("cB")));
    assert(removeVowels(("ybcd")).equals(("ybcd")));
    }

}
