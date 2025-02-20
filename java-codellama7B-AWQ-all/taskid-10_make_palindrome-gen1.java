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

        if (string == null) {
            throw new IllegalArgumentException();
        }
        // Find the longest postfix of the supplied string that is a palindrome.
        String palindrome = "";
        for (int i = string.length(); i > 0; i--) {
            String prefix = string.substring(0, i);
            if (prefix.equals(prefix.reverse())) {
                palindrome = prefix;
                break;
            }
        }
        // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
        return string + palindrome.reverse().substring(0, palindrome.length() - 1);
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
