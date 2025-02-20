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

        String answer = "";
        char[] message_chars = message.toCharArray();
        for (int i = 0; i < message_chars.length; i++) {
            if (message_chars[i] >= 'A' && message_chars[i] <= 'Z') {
                answer += (char)(message_chars[i] + 32);
            } else if (message_chars[i] >= 'a' && message_chars[i] <= 'z') {
                answer += (char)(message_chars[i] - 32);
            } else {
                answer += message_chars[i];
            }
        }
        char[] answer_chars = answer.toCharArray();
        for (int i = 0; i < answer_chars.length; i++) {
            if (answer_chars[i] == 'a' || answer_chars[i] == 'e' || answer_chars[i] == 'i' || answer_chars[i] == 'o' || answer_chars[i] == 'u') {
                answer_chars[i] = (char)((answer_chars[i] + 2 - 'a') + 'a');
            } else if (answer_chars[i] == 'A' || answer_chars[i] == 'E' || answer_chars[i] == 'I' || answer_chars[i] == 'O' || answer_chars[i] == 'U') {
                answer_chars[i] = (char)((answer_chars[i] + 2 - 'A') + 'A');
            }
        }
        return String.valueOf(answer_chars);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
