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
        String[] words = message.split(" ");
        for (int i = 0; i < words.length; i++) {
            encoded += words[i].toUpperCase();
        }
        String vowels = "AEIOU";
        String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String temp = "";
        for (int i = 0; i < encoded.length(); i++) {
            if (vowels.contains("" + encoded.charAt(i))) {
                temp = vowels.substring(vowels.indexOf("" + encoded.charAt(i)) + 2, vowels.indexOf("" + encoded.charAt(i)) + 3);
            }
            encoded = encoded.replace("" + encoded.charAt(i), temp);
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
