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

        // Find the longest postfix that is a palindrome.
        String palindrome = string;
        for (int i = string.length() - 1; i >= 0; i--) {
            if (string.charAt(i) != string.charAt(string.length() - 1)) {
                palindrome = string.substring(0, i + 1);
                break;
            }
        }
        // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
        StringBuilder sb = new StringBuilder(string);
        int length = sb.length();
        for (int i = palindrome.length() - 1; i >= 0; i--) {
            sb.append(string.charAt(length - palindrome.length() + i));
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
