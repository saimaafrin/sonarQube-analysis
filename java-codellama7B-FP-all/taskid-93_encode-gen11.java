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

        char[] messageCharArray = message.toCharArray();
        char[] outputArray = new char[messageCharArray.length];
        for (int i = 0; i < messageCharArray.length; i++) {
            if (isVowel(messageCharArray[i])) {
                int index = getVowelIndex(messageCharArray[i]) + 2;
                outputArray[i] = getCharFromAlphabet(index);
            } else {
                outputArray[i] = Character.isUpperCase(messageCharArray[i]) ? Character.toLowerCase(messageCharArray[i]) : Character.toUpperCase(messageCharArray[i]);
            }
        }
        String output = String.valueOf(outputArray);
        return output;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
