import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes a message, and encodes in such a 
    // way that it swaps case of all letters, replaces all vowels in 
    // the message with the letter that appears 2 places ahead of that 
    // vowel in the english alphabet. 
    // Assume only letters. 
    // Examples:
    // >>> encode(("test"))
    // ("TGST")
    // >>> encode(("This is a message"))
    // ("tHKS KS C MGSSCGG")
    public static String encode(String message) {

        String encoded = "";
        String encodedLower = "";
        String encodedUpper = "";
        String encodedVowels = "";
        String encodedConsonants = "";
        int vowelPosition = 0;
        int consonantPosition = 0;
        for (int i = 0; i < message.length(); i++) {
            if (message.charAt(i) == ' ') {
                encoded += ' ';
            } else if (message.charAt(i) >= 97 && message.charAt(i) <= 122) {
                encodedLower += message.charAt(i);
            } else if (message.charAt(i) >= 65 && message.charAt(i) <= 90) {
                encodedUpper += message.charAt(i);
            }
        }
        for (int i = 0; i < encodedLower.length(); i++) {
            if (encodedLower.charAt(i) == 'a' || encodedLower.charAt(i) == 'e' || encodedLower.charAt(i) == 'i' || encodedLower.charAt(i) == 'o' || encodedLower.charAt(i) == 'u') {
                vowelPosition = i;
                encodedVowels += encodedLower.charAt(vowelPosition);
                consonantPosition = vowelPosition + 2;
                encodedConsonants += encodedLower.charAt(consonantPosition);
            } else {
                encodedConsonants += encodedLower.charAt(i);
            }
        }
        for (int i = 0; i < encodedUpper.length(); i++) {
            if (encodedUpper.charAt(i) == 'A' || encodedUpper.charAt(i) == 'E' || encodedUpper.charAt(i) == 'I' || encodedUpper.charAt(i) == 'O' || encodedUpper.charAt(i) == 'U') {
                vowelPosition = i;
                encodedVowels += encodedUpper.charAt(vowelPosition);
                consonantPosition = vowelPosition + 2;
                encodedConsonants += encodedUpper.charAt(consonantPosition);
            } else {
                encodedConsonants += encodedUpper.charAt(i);
            }
        }
        encoded = encodedVowels + encodedConsonants;
        return encoded;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
