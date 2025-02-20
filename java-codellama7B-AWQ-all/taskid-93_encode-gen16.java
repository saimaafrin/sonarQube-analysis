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

        char[] msg = message.toCharArray();
        for (int i = 0; i < msg.length; i++) {
            if (msg[i] >= 'a' && msg[i] <= 'z') {
                msg[i] = (char)(msg[i] - ('a' - 'A'));
            } else if (msg[i] >= 'A' && msg[i] <= 'Z') {
                msg[i] = (char)(msg[i] + ('a' - 'A'));
            }
            if (msg[i] == 'a' || msg[i] == 'e' || msg[i] == 'i' || msg[i] == 'o' || msg[i] == 'u' || msg[i] == 'A' || msg[i] == 'E' || msg[i] == 'I' || msg[i] == 'O' || msg[i] == 'U') {
                msg[i] = (char)((msg[i] + 2) % 26 + 'A');
            }
        }
        return String.valueOf(msg);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
