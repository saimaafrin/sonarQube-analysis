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

        char[] result = message.toCharArray();
        for (int i = 0; i < result.length; i++) {
            char c = result[i];
            if ((c >= 'A') && (c <= 'Z')) {
                c = (char)(c + 'a' - 'A');
            } else if ((c >= 'a') && (c <= 'z')) {
                c = (char)(c + 'A' - 'a');
            }
            if ((c >= 'a') && (c <= 'z')) {
                switch (c) {
                case 'a':
                    c = 'd';
                    break;
                case 'c':
                    c = 'e';
                    break;
                case 'e':
                    c = 'f';
                    break;
                case 'g':
                    c = 'h';
                    break;
                case 'i':
                    c = 'j';
                    break;
                case 'k':
                    c = 'l';
                    break;
                case 'm':
                    c = 'n';
                    break;
                case 'o':
                    c = 'p';
                    break;
                case 'q':
                    c = 'r';
                    break;
                case 's':
                    c = 't';
                    break;
                case 'u':
                    c = 'v';
                    break;
                case 'v':
                    c = 'w';
                    break;
                case 'x':
                    c = 'y';
                    break;
                case 'y':
                    c = 'z';
                    break;
                case 'z':
                    c = 'a';
                    break;
                }
            }
            result[i] = c;
        }
        return String.valueOf(result);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
