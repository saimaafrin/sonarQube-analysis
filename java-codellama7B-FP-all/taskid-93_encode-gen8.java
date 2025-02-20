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
        String msg = "";
        for (int i = 0; i < message.length(); i++) {
            if (Character.isLetter(message.charAt(i))) {
                msg += message.charAt(i);
            }
        }
        for (int i = 0; i < msg.length(); i++) {
            if (Character.isUpperCase(msg.charAt(i))) {
                encoded += Character.toLowerCase(msg.charAt(i));
            } else {
                encoded += Character.toUpperCase(msg.charAt(i));
            }
        }
        for (int i = 0; i < encoded.length(); i++) {
            if (encoded.charAt(i) == 'A' || encoded.charAt(i) == 'a' || encoded.charAt(i) == 'E' || encoded.charAt(i) == 'e' || encoded.charAt(i) == 'I' || encoded.charAt(i) == 'i' || encoded.charAt(i) == 'O' || encoded.charAt(i) == 'o' || encoded.charAt(i) == 'U' || encoded.charAt(i) == 'u') {
                if (i + 2 <= encoded.length()) {
                    encoded = encoded.substring(0, i) + Character.toUpperCase(encoded.charAt(i + 2)) + encoded.substring(i + 3);
                }
            } else {
                encoded = encoded.substring(0, i) + Character.toLowerCase(encoded.charAt(i + 2)) + encoded.substring(i + 3);
            }
        }
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
