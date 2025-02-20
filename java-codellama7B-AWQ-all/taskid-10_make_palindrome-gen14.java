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

        if (string == null || string.length() == 0) {
            return string;
        }
        StringBuilder sb = new StringBuilder(string);
        String reverse = sb.reverse().toString();
        if (string.endsWith(reverse)) {
            return string;
        }
        int i = 1;
        while (i < string.length() && string.substring(0, i).equals(string.substring(string.length() - i, string.length()))) {
            i++;
        }
        String prefix = string.substring(0, string.length() - i + 1);
        String suffix = reverse.substring(0, i - 1);
        sb = new StringBuilder(prefix);
        sb.append(suffix);
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
