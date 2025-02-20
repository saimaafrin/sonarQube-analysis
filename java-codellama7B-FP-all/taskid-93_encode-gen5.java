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
        int i = 0;
        int j = 0;
        char temp;
        for (i = 0; i < message.length(); i++) {
            if (Character.isUpperCase(message.charAt(i))) {
                temp = (char) (message.charAt(i) + 32);
            } else {
                temp = (char) (message.charAt(i) - 32);
            }
            encoded = encoded + temp;
        }
        char[] encodedArray = encoded.toCharArray();
        for (i = 0; i < message.length(); i++) {
            if (message.charAt(i) == 'a' || message.charAt(i) == 'e' || message.charAt(i) == 'i' || message.charAt(i) == 'o' || message.charAt(i) == 'u' || message.charAt(i) == 'A' || message.charAt(i) == 'E' || message.charAt(i) == 'I' || message.charAt(i) == 'O' || message.charAt(i) == 'U') {
                j = i + 2;
                encodedArray[i] = (char) (encodedArray[j]);
            }
        }
        encoded = new String(encodedArray);
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
