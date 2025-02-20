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

        if (number <= 0) {
            return "";
        }
        List<String> roman = new ArrayList<String>();
        while (number > 0) {
            if (number >= 1000) {
                roman.add("m");
                number -= 1000;
            } else if (number >= 900) {
                roman.add("cm");
                number -= 900;
            } else if (number >= 500) {
                roman.add("d");
                number -= 500;
            } else if (number >= 400) {
                roman.add("cd");
                number -= 400;
            } else if (number >= 100) {
                roman.add("c");
                number -= 100;
            } else if (number >= 90) {
                roman.add("xc");
                number -= 90;
            } else if (number >= 50) {
                roman.add("l");
                number -= 50;
            } else if (number >= 40) {
                roman.add("xl");
                number -= 40;
            } else if (number >= 10) {
                roman.add("x");
                number -= 10;
            } else if (number >= 9) {
                roman.add("ix");
                number -= 9;
            } else if (number >= 5) {
                roman.add("v");
                number -= 5;
            } else if (number >= 4) {
                roman.add("iv");
                number -= 4;
            } else if (number >= 1) {
                roman.add("i");
                number -= 1;
            }
        }
        StringBuilder builder = new StringBuilder();
        for (String s : roman) {
            builder.append(s);
        }
        return builder.toString();
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
