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

        char[] newMessage = new char[message.length()];
        int count = 0;
        int index = 0;
        for(int i = 0; i < message.length(); i++) {
            if(message.charAt(i) == 'a' || message.charAt(i) == 'A') {
                newMessage[index] = 'c';
                count++;
            } else if(message.charAt(i) == 'e' || message.charAt(i) == 'E') {
                newMessage[index] = 'g';
                count++;
            } else if(message.charAt(i) == 'i' || message.charAt(i) == 'I') {
                newMessage[index] = 'k';
                count++;
            } else if(message.charAt(i) == 'o' || message.charAt(i) == 'O') {
                newMessage[index] = 'm';
                count++;
            } else if(message.charAt(i) == 'u' || message.charAt(i) == 'U') {
                newMessage[index] = 's';
                count++;
            } else {
                newMessage[index] = message.charAt(i);
            }
            index++;
        }
        return String.valueOf(newMessage);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
