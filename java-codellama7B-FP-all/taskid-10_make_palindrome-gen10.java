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

        int i;
        int j;
        // Find longest postfix of the supplied string that is a palindrome.
        for (i = string.length(); i > 0; i--) {
            if (isPalindrome(string.substring(0, i))) {
                break;
            }
        }
        // If postfix was found, append to it reverse of the prefix that comes before it.
        if (i > 0) {
            return string + new StringBuffer(string.substring(0, i)).reverse();
        }
        // If postfix was not found, append to the end of the supplied string a prefix that comes before it.
        else {
            for (j = string.length(); j > 0; j--) {
                if (isPalindrome(string.substring(j))) {
                    break;
                }
            }
            return string + string.substring(0, j);
        }
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
