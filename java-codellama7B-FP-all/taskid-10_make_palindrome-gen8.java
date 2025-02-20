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

        String result = "";
        // Find the longest postfix of the supplied string that is a palindrome.
        // For example, if supplied string is "cata", then its postfix "a" is a palindrome.
        // "a" is the longest palindrome.
        for (int i = string.length() - 1; i >= 0; --i) {
            int j = i;
            while (j >= 0 && string.charAt(j) == string.charAt(string.length() - 1 - j)) {
                j--;
            }
            // If the current position in the string (i) is greater or equal to the last position in the palindrome (j),
            // then the current position is also the last position in the palindrome, and we have found the longest palindrome.
            if (i >= j) {
                result = string.substring(i, string.length()) + string.substring(0, j + 1);
                break;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
