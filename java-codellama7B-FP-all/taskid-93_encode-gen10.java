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

        StringBuffer encodedMessage = new StringBuffer();
        boolean isVowel = false;
        for (int i = 0; i < message.length(); i++) {
            if (message.charAt(i) == 'a' || message.charAt(i) == 'e' || message.charAt(i) == 'i' || message.charAt(i) == 'o' || message.charAt(i) == 'u') {
                isVowel = true;
            }
            if (message.charAt(i) == 'A' || message.charAt(i) == 'E' || message.charAt(i) == 'I' || message.charAt(i) == 'O' || message.charAt(i) == 'U') {
                isVowel = false;
            }
            if (isVowel) {
                if (message.charAt(i) == 'a') {
                    encodedMessage.append((char)('c'));
                }
                else if (message.charAt(i) == 'e') {
                    encodedMessage.append((char)('g'));
                }
                else if (message.charAt(i) == 'i') {
                    encodedMessage.append((char)('k'));
                }
                else if (message.charAt(i) == 'o') {
                    encodedMessage.append((char)('m'));
                }
                else if (message.charAt(i) == 'u') {
                    encodedMessage.append((char)('s'));
                }
            }
            else {
                if (message.charAt(i) >= 'A' && message.charAt(i) <= 'Z') {
                    encodedMessage.append((char)(((message.charAt(i) + 2) - 65)));
                }
                else {
                    encodedMessage.append((char)(((message.charAt(i) + 2) - 97)));
                }
            }
        }
        return encodedMessage.toString();
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
