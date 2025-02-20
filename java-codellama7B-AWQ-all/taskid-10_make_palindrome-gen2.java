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

        String palindrome = "";
        String reversed = new StringBuffer(string).reverse().toString();
        int longestCommonPrefix = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == reversed.charAt(i)) {
                longestCommonPrefix++;
            } else {
                break;
            }
        }
        palindrome = string.substring(0, longestCommonPrefix);
        String palindromePrefix = palindrome.substring(0, palindrome.length() / 2);
        String palindromeSuffix = string.substring(longestCommonPrefix);
        String suffixReversed = new StringBuffer(palindromeSuffix).reverse().toString();
        for (int i = 0; i < palindromeSuffix.length(); i++) {
            if (palindromeSuffix.charAt(i) == suffixReversed.charAt(i)) {
                palindrome += palindromePrefix.charAt(palindromePrefix.length() - 1 - i);
            } else {
                break;
            }
        }
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
