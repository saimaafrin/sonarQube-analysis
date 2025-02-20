import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Checks if given string is a palindrome
    // >>> isPalindrome((""))
    // (true)
    // >>> isPalindrome(("aba"))
    // (true)
    // >>> isPalindrome(("aaaaa"))
    // (true)
    // >>> isPalindrome(("zbcd"))
    // (false)
    public static boolean isPalindrome(String text) {

        // Initialize empty string
        StringBuilder palindrome = new StringBuilder();
        // For each character in text
        for (int i = 0; i < text.length(); i++) {
            // Add character to palindrome
            palindrome.append(text.charAt(i));
        }
        // For each character in palindrome
        for (int i = 0; i < palindrome.length(); i++) {
            // If character does not match
            if (palindrome.charAt(i) != palindrome.charAt(palindrome.length() - 1 - i)) {
                // Return false
                return false;
            }
        }
        // Return true
        return true;
    }
    public static void main(String[] args) {
    assert(isPalindrome(("")) == (true));
    assert(isPalindrome(("aba")) == (true));
    assert(isPalindrome(("aaaaa")) == (true));
    assert(isPalindrome(("zbcd")) == (false));
    assert(isPalindrome(("xywyx")) == (true));
    assert(isPalindrome(("xywyz")) == (false));
    assert(isPalindrome(("xywzx")) == (false));
    }

}
