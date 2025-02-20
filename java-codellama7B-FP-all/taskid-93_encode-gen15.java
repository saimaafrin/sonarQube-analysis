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

        String output = "";
        int aPos = 0, ePos = 0, iPos = 0, oPos = 0, uPos = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (vowels.contains("" + c)) {
                if (c == 'a') {
                    output += "" + vowels.charAt(aPos += 2);
                } else if (c == 'e') {
                    output += "" + vowels.charAt(ePos += 2);
                } else if (c == 'i') {
                    output += "" + vowels.charAt(iPos += 2);
                } else if (c == 'o') {
                    output += "" + vowels.charAt(oPos += 2);
                } else if (c == 'u') {
                    output += "" + vowels.charAt(uPos += 2);
                }
            } else {
                output += Character.toUpperCase(c);
            }
        }
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
