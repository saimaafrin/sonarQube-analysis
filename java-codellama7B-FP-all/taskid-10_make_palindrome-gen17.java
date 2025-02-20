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

        String suffix = "";
        String prefix = "";
        int len = string.length();
        for (int i = len - 1; i >= 0; i--) {
            if (string.charAt(i) == string.charAt(len - 1)) {
                suffix = string.substring(i);
                break;
            }
        }
        for (int i = 0; i < len - 1; i++) {
            if (string.charAt(i) == string.charAt(len - 1)) {
                prefix = string.substring(i + 1);
                break;
            }
        }
        return string + new StringBuilder(prefix).reverse().toString() + suffix;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
