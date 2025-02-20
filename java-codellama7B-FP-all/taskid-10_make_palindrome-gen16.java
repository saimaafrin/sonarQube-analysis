import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Find the shortest palindrome that begins with a supplied string.
    // Algorithm idea is simple:
    // - Find the longest postfix of supplied string that is a palindrome.
    // - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    // >>> makePalindrome((""))
    // ("")
    // >>> makePalindrome(("cat"))
    // ("catac")
    // >>> makePalindrome(("cata"))
    // ("catac")
    public static String makePalindrome(String string) {

        String postfix = "", prefix = "";
        String palindrome = "";
        String revPrefix = "";
        String revPostfix = "";
        for (int i = 0; i < string.length(); i++) {
            if (isPalindrome(string.substring(0, i + 1))) {
                postfix = string.substring(0, i + 1);
            }
        }
        for (int j = string.length() - 1; j >= 0; j--) {
            if (isPalindrome(string.substring(0, j + 1))) {
                prefix = string.substring(0, j + 1);
            }
        }
        revPrefix = new StringBuilder(prefix).reverse().toString();
        revPostfix = new StringBuilder(postfix).reverse().toString();
        palindrome = revPrefix + string + revPostfix;
        return palindrome;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
