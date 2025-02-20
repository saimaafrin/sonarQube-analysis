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

        String codedMessage = "";
        char[] array = message.toCharArray();
        for (int i = 0; i < array.length; i++) {
            if (Character.isUpperCase(array[i])) {
                codedMessage += Character.toLowerCase(array[i]);
            } else {
                codedMessage += Character.toUpperCase(array[i]);
            }
        }
        for (int i = 0; i < codedMessage.length(); i++) {
            if (codedMessage.charAt(i) == 'a' || codedMessage.charAt(i) == 'A') {
                codedMessage = codedMessage.substring(0, i) + "c" + codedMessage.substring(i + 1);
            } else if (codedMessage.charAt(i) == 'e' || codedMessage.charAt(i) == 'E') {
                codedMessage = codedMessage.substring(0, i) + "g" + codedMessage.substring(i + 1);
            } else if (codedMessage.charAt(i) == 'i' || codedMessage.charAt(i) == 'I') {
                codedMessage = codedMessage.substring(0, i) + "h" + codedMessage.substring(i + 1);
            } else if (codedMessage.charAt(i) == 'o' || codedMessage.charAt(i) == 'O') {
                codedMessage = codedMessage.substring(0, i) + "n" + codedMessage.substring(i + 1);
            } else if (codedMessage.charAt(i) == 'u' || codedMessage.charAt(i) == 'U') {
                codedMessage = codedMessage.substring(0, i) + "r" + codedMessage.substring(i + 1);
            }
        }
        return codedMessage;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
