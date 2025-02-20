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

        // Write your solution here
        final List<String> romanNumerals = new ArrayList<String>() {{
            add("M");
            add("CM");
            add("D");
            add("CD");
            add("C");
            add("XC");
            add("L");
            add("XL");
            add("X");
            add("IX");
            add("V");
            add("IV");
            add("I");
        }};
        final List<Long> values = new ArrayList<Long>() {{
            add(1000l);
            add(900l);
            add(500l);
            add(400l);
            add(100l);
            add(90l);
            add(50l);
            add(40l);
            add(10l);
            add(9l);
            add(5l);
            add(4l);
            add(1l);
            add(0l);
        }};
        String s = "";
        long i = 0l;
        while (number > 0l) {
            while ((number - values.get(i)) >= 0l) {
                number -= values.get(i);
                s += romanNumerals.get(i);
            }
            i++;
        }
        return s;
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
