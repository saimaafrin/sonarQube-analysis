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
        // Find the longest postfix of supplied string that is a palindrome.
        // This is done by trying to append each symbol from end to start of the string to itself.
        int m = n;
        for (int i = n - 1; i >= 0; i--) {
            if (string.charAt(i) == string.charAt(n - 1)) {
                m = i + 1;
            }
        }
        String prefix = string.substring(0, m);
        String suffix = string.substring(m, n);
        StringBuilder sb = new StringBuilder(string);
        sb.reverse().append(suffix).append(prefix).append(suffix);
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
