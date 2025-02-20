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

        int n = string.length();
        // Find the longest postfix of string that is a palindrome
        String postfix = string;
        for (int i = n - 1; i >= 0; i--) {
            if (isPalindrome(postfix, 0, i)) {
                postfix = postfix.substring(0, i + 1);
                break;
            }
        }
        // Find the longest prefix of string that is a palindrome
        String prefix = string;
        for (int i = 1; i < n; i++) {
            if (isPalindrome(prefix, i, n - 1)) {
                prefix = prefix.substring(i);
                break;
            }
        }
        // Append to the end of the string the reverse of a string prefix that comes before the palindromic suffix
        return prefix + new StringBuilder(postfix).reverse().toString();
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
