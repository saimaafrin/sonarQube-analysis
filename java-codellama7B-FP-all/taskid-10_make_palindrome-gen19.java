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

        // TODO: Implement the solution here.
        //return "";
        String s = string.toLowerCase();
        String rev = new StringBuilder(s).reverse().toString();
        String suffix = "", prefix = "";
        for (int i = s.length(); i >= 0; i--) {
            if (s.substring(0, i).equals(rev.substring(0, i))) {
                suffix = rev.substring(0, i);
                break;
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(i).equals(rev.substring(0, s.length() - i))) {
                prefix = rev.substring(0, s.length() - i);
                break;
            }
        }
        return s + prefix + suffix;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
