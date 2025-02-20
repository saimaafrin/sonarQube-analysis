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

        char[] chars = message.toCharArray();
        int index = 0;
        for (int i = 0; i < chars.length; i++) {
            if (Character.isUpperCase(chars[i])) {
                chars[i] = Character.toLowerCase(chars[i]);
            } else {
                chars[i] = Character.toUpperCase(chars[i]);
            }
            index = i;
        }
        for (int i = 0; i < chars.length; i++) {
            if (Character.isLetter(chars[i])) {
                switch (chars[i]) {
                    case 'a':
                        chars[i] = 'c';
                        break;
                    case 'c':
                        chars[i] = 'a';
                        break;
                    case 'e':
                        chars[i] = 'g';
                        break;
                    case 'g':
                        chars[i] = 'e';
                        break;
                    case 'i':
                        chars[i] = 'k';
                        break;
                    case 'k':
                        chars[i] = 'i';
                        break;
                    case 'o':
                        chars[i] = 'q';
                        break;
                    case 'q':
                        chars[i] = 'o';
                        break;
                    case 'u':
                        chars[i] = 'x';
                        break;
                    case 'x':
                        chars[i] = 'u';
                        break;
                    case 'z':
                        chars[i] = 'z';
                        break;
                    default:
                        chars[i] = Character.toLowerCase(chars[i]);
                        break;
                }
            }
        }
        return String.valueOf(chars);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
