import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function that returns true if the last character
    // of a given string is an alphabetical character and is not
    // a part of a word, and false otherwise.
    // Note: "word" is a group of characters separated by space.
    // Examples:
    // >>> checkIfLastCharIsALetter(("apple pie"))
    // (false)
    // >>> checkIfLastCharIsALetter(("apple pi e"))
    // (true)
    // >>> checkIfLastCharIsALetter(("apple pi e "))
    // (false)
    // >>> checkIfLastCharIsALetter((""))
    // (false)
    public static boolean checkIfLastCharIsALetter(String txt) {

        // String[] words = txt.split(" ");
        boolean result = false;
        // if (words.length == 1) {
        //     char lastChar = txt.charAt(txt.length() - 1);
        //     result = Character.isLetter(lastChar);
        // } else {
        //     char lastChar = txt.charAt(txt.length() - 1);
        //     if (Character.isLetter(lastChar) && !txt.contains(" ")) {
        //         result = true;
        //     } else {
        //         result = false;
        //     }
        // }
        if (txt.contains(" ")) {
            String[] words = txt.split(" ");
            String[] tmp = words[words.length - 1].split("");
            char lastChar = tmp[tmp.length - 1].charAt(0);
            if (Character.isLetter(lastChar)) {
                result = true;
            } else {
                result = false;
            }
        } else {
            char lastChar = txt.charAt(txt.length() - 1);
            if (Character.isLetter(lastChar)) {
                result = true;
            } else {
                result = false;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(checkIfLastCharIsALetter(("apple")) == (false));
    assert(checkIfLastCharIsALetter(("apple pi e")) == (true));
    assert(checkIfLastCharIsALetter(("eeeee")) == (false));
    assert(checkIfLastCharIsALetter(("A")) == (true));
    assert(checkIfLastCharIsALetter(("Pumpkin pie ")) == (false));
    assert(checkIfLastCharIsALetter(("Pumpkin pie 1")) == (false));
    assert(checkIfLastCharIsALetter(("")) == (false));
    assert(checkIfLastCharIsALetter(("eeeee e ")) == (false));
    assert(checkIfLastCharIsALetter(("apple pie")) == (false));
    assert(checkIfLastCharIsALetter(("apple pi e ")) == (false));
    }

}
