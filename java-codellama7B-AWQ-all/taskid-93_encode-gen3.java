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

        int position = 0;
        int nextPosition = 0;
        char nextCharacter = ' ';
        char nextNextCharacter = ' ';
        char nextNextNextCharacter = ' ';
        String encodedMessage = "";
        for (int i = 0; i < message.length(); i++) {
            position = message.charAt(i) - 'a';
            if (position >= 0 && position <= 25) {
                nextPosition = position + 2;
                nextNextPosition = position + 3;
                nextNextNextPosition = position + 4;
                if (nextPosition >= 0 && nextPosition <= 25) {
                    nextCharacter = (char) (position + 97);
                } else {
                    nextCharacter = (char) (nextPosition - 26 + 97);
                }
                if (nextNextPosition >= 0 && nextNextPosition <= 25) {
                    nextNextCharacter = (char) (nextNextPosition + 97);
                } else {
                    nextNextCharacter = (char) (nextNextPosition - 26 + 97);
                }
                if (nextNextNextPosition >= 0 && nextNextNextPosition <= 25) {
                    nextNextNextCharacter = (char) (nextNextNextPosition + 97);
                } else {
                    nextNextNextCharacter = (char) (nextNextNextPosition - 26 + 97);
                }
                encodedMessage += String.valueOf(nextNextNextCharacter);
            }
        }
        return encodedMessage;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
