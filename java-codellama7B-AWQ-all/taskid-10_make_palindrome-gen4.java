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

        if (string.length() == 0) return string;
        int length = string.length();
        StringBuilder result = new StringBuilder(length);
        // Find the longest postfix of the string that is a palindrome.
        // If the string is palindrome by itself, this postfix will be the entire string.
        int i = 0;
        while (i < length) {
            int j = i;
            while (j < length - j && string.charAt(j) == string.charAt(length - 1 - j)) j++;
            result.append(string.substring(i, length - j + 1));
            i = length - j + 1;
        }
        // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
        // If the string is palindrome by itself, there is no reverse prefix.
        if (i < length) {
            result.append(string.substring(0, i).reverse());
        }
        return result.toString();
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
