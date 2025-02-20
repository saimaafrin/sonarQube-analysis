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

        message = message.toLowerCase();
        char[] arr = message.toCharArray();
        char[] newArr = new char[arr.length];
        for(int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                int index = c - 'a';
                index += 2;
                index = index % 26;
                c = (char) ('a' + index);
            }
            else if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                int index = c - 'A';
                index += 2;
                index = index % 26;
                c = (char) ('A' + index);
            }
            newArr[i] = c;
        }
        return String.valueOf(newArr);
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
