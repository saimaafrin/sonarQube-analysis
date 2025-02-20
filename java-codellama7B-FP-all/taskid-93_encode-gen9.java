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

        char[] m = message.toCharArray();
        int j = 0;
        for(int i = 0; i < m.length; i++) {
            if(Character.isLetter(m[i])) {
                if(Character.isLowerCase(m[i])) {
                    m[j] = Character.toUpperCase(m[i]);
                } else {
                    m[j] = Character.toLowerCase(m[i]);
                }
                j++;
            } else {
                m[j] = m[i];
                j++;
            }
        }
        StringBuffer buffer = new StringBuffer();
        for(int i = 0; i < j; i++) {
            if(Character.isLetter(m[i])) {
                if(m[i] == 'a' || m[i] == 'e' || m[i] == 'i' || m[i] == 'o' || m[i] == 'u') {
                    buffer.append(Character.toChars(m[i] + 2));
                } else {
                    buffer.append(m[i]);
                }
            } else {
                buffer.append(m[i]);
            }
        }
        return buffer.toString();
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
