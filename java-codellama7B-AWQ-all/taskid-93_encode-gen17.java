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

        String newString = message;
        for(int i = 0; i < message.length(); i++) {
            if(message.charAt(i) == 'a') {
                newString = newString.replace(message.charAt(i), 'c');
            } else if(message.charAt(i) == 'e') {
                newString = newString.replace(message.charAt(i), 'g');
            } else if(message.charAt(i) == 'i') {
                newString = newString.replace(message.charAt(i), 'k');
            } else if(message.charAt(i) == 'o') {
                newString = newString.replace(message.charAt(i), 's');
            } else if(message.charAt(i) == 'u') {
                newString = newString.replace(message.charAt(i), 'x');
            } else if(message.charAt(i) == 'A') {
                newString = newString.replace(message.charAt(i), 'C');
            } else if(message.charAt(i) == 'E') {
                newString = newString.replace(message.charAt(i), 'G');
            } else if(message.charAt(i) == 'I') {
                newString = newString.replace(message.charAt(i), 'K');
            } else if(message.charAt(i) == 'O') {
                newString = newString.replace(message.charAt(i), 'S');
            } else if(message.charAt(i) == 'U') {
                newString = newString.replace(message.charAt(i), 'X');
            }
        }
        return newString;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
