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

        String result = "";
        String[] letters = message.split("");
        for(int i = 0; i < letters.length; i++){
            if(letters[i].equalsIgnoreCase("a"))
                result = result + "c";
            else if(letters[i].equalsIgnoreCase("e"))
                result = result + "d";
            else if(letters[i].equalsIgnoreCase("i"))
                result = result + "h";
            else if(letters[i].equalsIgnoreCase("o"))
                result = result + "n";
            else if(letters[i].equalsIgnoreCase("u"))
                result = result + "m";
            else if(letters[i].equalsIgnoreCase("A"))
                result = result + "C";
            else if(letters[i].equalsIgnoreCase("E"))
                result = result + "D";
            else if(letters[i].equalsIgnoreCase("I"))
                result = result + "H";
            else if(letters[i].equalsIgnoreCase("O"))
                result = result + "N";
            else if(letters[i].equalsIgnoreCase("U"))
                result = result + "M";
            else
                result = result + letters[i];
        }
        return result;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
