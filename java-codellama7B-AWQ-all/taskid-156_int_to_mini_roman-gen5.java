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

        String s = Long.toString(number);
        int len = s.length();
        String roman = "";
        int[] values = new int[len];
        // fill the values array with the corresponding number for each digit
        for (int i = 0; i < len; i++) {
            values[i] = s.charAt(i) - '0';
        }
        for (int i = 0; i < len; i++) {
            roman += values[i] == 0 ? "" :
                values[i] == 1 ? "i" :
                values[i] == 5 ? "v" :
                values[i] == 9 ? "ix" :
                values[i] == 4 ? "iv" :
                values[i] == 10 ? "x" :
                values[i] == 40 ? "xl" :
                values[i] == 90 ? "xci" :
                values[i] == 400 ? "cd" :
                values[i] == 900 ? "cm" :
                values[i] == 500 ? "d" :
                values[i] == 50 ? "l" :
                values[i] == 5000 ? "m" : "?";
        }
        return roman;
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
