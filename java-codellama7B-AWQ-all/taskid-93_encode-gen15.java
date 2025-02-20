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

      String str = "";
      for(int i = 0; i < message.length(); i++){
        if(i == 0){
          str += String.valueOf(Character.toUpperCase(message.charAt(i)));
        }
        else if(i == message.length()-1){
          str += String.valueOf(Character.toLowerCase(message.charAt(i)));
        }
        else{
          str += String.valueOf(Character.toLowerCase(message.charAt(i)));
        }
      }
      for(int i = 0; i < str.length(); i++){
        if(str.charAt(i) == 'a'){
          str = str.substring(0, i) + "c" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'e'){
          str = str.substring(0, i) + "g" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'i'){
          str = str.substring(0, i) + "h" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'o'){
          str = str.substring(0, i) + "j" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'u'){
          str = str.substring(0, i) + "n" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'A'){
          str = str.substring(0, i) + "C" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'E'){
          str = str.substring(0, i) + "G" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'I'){
          str = str.substring(0, i) + "H" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'O'){
          str = str.substring(0, i) + "J" + str.substring(i+1);
        }
        else if(str.charAt(i) == 'U'){
          str = str.substring(0, i) + "N" + str.substring(i+1);
        }
      }
      return str;
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
