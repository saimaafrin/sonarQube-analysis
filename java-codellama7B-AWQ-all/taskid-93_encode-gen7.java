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

        // Solution:
        //  1. convert to list
        //  2. replace vowels with next char
        //  3. convert back to String
        String answer = message.toLowerCase()
            .chars()
            .map(c -> (char)c)
            .map(c -> c == 'a' ? 'b'
                        : c == 'b' ? 'c'
                        : c == 'c' ? 'd'
                        : c == 'd' ? 'e'
                        : c == 'e' ? 'f'
                        : c == 'f' ? 'g'
                        : c == 'g' ? 'h'
                        : c == 'h' ? 'i'
                        : c == 'i' ? 'j'
                        : c == 'j' ? 'k'
                        : c == 'k' ? 'l'
                        : c == 'l' ? 'm'
                        : c == 'm' ? 'n'
                        : c == 'n' ? 'o'
                        : c == 'o' ? 'p'
                        : c == 'p' ? 'q'
                        : c == 'q' ? 'r'
                        : c == 'r' ? 's'
                        : c == 's' ? 't'
                        : c == 't' ? 'u'
                        : c == 'u' ? 'v'
                        : c == 'v' ? 'w'
                        : c == 'w' ? 'x'
                        : c == 'x' ? 'y'
                        : c == 'y' ? 'z'
                        : c == 'z' ? 'a'
                        : c
                        )
            .mapToObj(c -> (char)c)
            .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
            .toString()
            .toUpperCase();
        return answer;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
