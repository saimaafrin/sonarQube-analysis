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

        // Find the longest postfix of supplied string that is a palindrome.
        String longestPalindromicPostfix = "";
        int n = string.length();
        for (int i = 0; i < n; i++) {
            String postfix = string.substring(i, n);
            if (isPalindrome(postfix)) {
                longestPalindromicPostfix = postfix;
                n = i;
            }
        }
        // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
        String prefix = string.substring(0, n);
        String suffix = new StringBuilder(longestPalindromicPostfix).reverse().toString();
        return prefix + suffix;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
