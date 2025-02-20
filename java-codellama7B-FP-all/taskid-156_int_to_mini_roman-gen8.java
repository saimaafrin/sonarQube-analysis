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

        Map<Long, String> numbers = new HashMap<Long, String>();
        numbers.put((long)1, "i");
        numbers.put((long)4, "iv");
        numbers.put((long)5, "v");
        numbers.put((long)9, "ix");
        numbers.put((long)10, "x");
        numbers.put((long)40, "xl");
        numbers.put((long)50, "l");
        numbers.put((long)90, "xci");
        numbers.put((long)100, "c");
        numbers.put((long)400, "cd");
        numbers.put((long)500, "d");
        numbers.put((long)900, "cm");
        numbers.put((long)1000, "m");

        StringBuilder roman = new StringBuilder();
        int i = 0;
        while (number > 0) {
            while (number >= numbers.get(Long.valueOf(Math.pow(10, i)))) {
                roman.append(numbers.get(Long.valueOf(Math.pow(10, i))));
                number -= Long.valueOf(Math.pow(10, i));
            }
            i++;
        }
        return roman.toString();
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
