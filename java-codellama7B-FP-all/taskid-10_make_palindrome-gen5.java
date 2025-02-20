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

        String palindromicSuffix = "";
        String palindromicPrefix = "";
        int longestPalindromicSuffixLength = 0;
        for (int i = 0; i < string.length(); i++) {
            String suffix = string.substring(i);
            if (suffix.equals(new StringBuilder(suffix).reverse().toString())) {
                palindromicSuffix = suffix;
                longestPalindromicSuffixLength = suffix.length();
            }
        }
        for (int i = string.length() - 1; i >= 0; i--) {
            String prefix = string.substring(0, i + 1);
            if (prefix.equals(new StringBuilder(prefix).reverse().toString())) {
                palindromicPrefix = prefix;
                break;
            }
        }
        return string + new StringBuilder(palindromicPrefix).reverse().toString().substring(0, string.length() - longestPalindromicSuffixLength);
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
