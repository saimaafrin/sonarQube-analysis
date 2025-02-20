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

        String encode="";
        for(int i=0;i<message.length();i++){
            if(message.charAt(i)=='a'){
                encode+=(char)(message.charAt(i)+2);
            }
            else if(message.charAt(i)=='e'){
                encode+=(char)(message.charAt(i)+4);
            }
            else if(message.charAt(i)=='i'){
                encode+=(char)(message.charAt(i)+1);
            }
            else if(message.charAt(i)=='o'){
                encode+=(char)(message.charAt(i)+2);
            }
            else if(message.charAt(i)=='u'){
                encode+=(char)(message.charAt(i)+4);
            }
            else if(message.charAt(i)=='A'){
                encode+=(char)(message.charAt(i)+2);
            }
            else if(message.charAt(i)=='E'){
                encode+=(char)(message.charAt(i)+4);
            }
            else if(message.charAt(i)=='I'){
                encode+=(char)(message.charAt(i)+1);
            }
            else if(message.charAt(i)=='O'){
                encode+=(char)(message.charAt(i)+2);
            }
            else if(message.charAt(i)=='U'){
                encode+=(char)(message.charAt(i)+4);
            }
            else{
                encode+=Character.toUpperCase(message.charAt(i));
            }
        }
        return encode;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
