import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer, obtain its roman numeral equivalent as a string,
    // and return it in lowercase.
    // Restrictions: 1 <= num <= 1000
    // Examples:
    // >>> intToMiniRoman((19l))
    // ("xix")
    // >>> intToMiniRoman((152l))
    // ("clii")
    // >>> intToMiniRoman((426l))
    // ("cdxxvi")
    public static String intToMiniRoman(long number) {

        String romanNumeral = "";
        while (number > 0) {
            if (number >= 1000) {
                romanNumeral += "m";
                number -= 1000;
            }
            else if (number >= 500) {
                romanNumeral += "d";
                number -= 500;
            }
            else if (number >= 100) {
                romanNumeral += "c";
                number -= 100;
            }
            else if (number >= 50) {
                romanNumeral += "l";
                number -= 50;
            }
            else if (number >= 10) {
                romanNumeral += "x";
                number -= 10;
            }
            else if (number >= 5) {
                romanNumeral += "v";
                number -= 5;
            }
            else if (number >= 1) {
                romanNumeral += "i";
                number -= 1;
            }
        }
        return romanNumeral;
    }
    public static void main(String[] args) {
    assert(intToMiniRoman((19l)).equals(("xix")));
    assert(intToMiniRoman((152l)).equals(("clii")));
    assert(intToMiniRoman((251l)).equals(("ccli")));
    assert(intToMiniRoman((426l)).equals(("cdxxvi")));
    assert(intToMiniRoman((500l)).equals(("d")));
    assert(intToMiniRoman((1l)).equals(("i")));
    assert(intToMiniRoman((4l)).equals(("iv")));
    assert(intToMiniRoman((43l)).equals(("xliii")));
    assert(intToMiniRoman((90l)).equals(("xc")));
    assert(intToMiniRoman((94l)).equals(("xciv")));
    assert(intToMiniRoman((532l)).equals(("dxxxii")));
    assert(intToMiniRoman((900l)).equals(("cm")));
    assert(intToMiniRoman((994l)).equals(("cmxciv")));
    assert(intToMiniRoman((1000l)).equals(("m")));
    }

}
