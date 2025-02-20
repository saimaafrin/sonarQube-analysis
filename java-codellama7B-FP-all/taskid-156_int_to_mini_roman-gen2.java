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

        if (number < 1 || number > 1000)
            throw new IllegalArgumentException("invalid number");
        char[] roman = new char[1000];
        int i = 0;
        for (; number >= 1000; number -= 1000)
            roman[i++] = 'm';
        for (; number >= 500; number -= 500)
            roman[i++] = 'd';
        for (; number >= 100; number -= 100)
            roman[i++] = 'c';
        for (; number >= 50; number -= 50)
            roman[i++] = 'l';
        for (; number >= 10; number -= 10)
            roman[i++] = 'x';
        for (; number >= 5; number -= 5)
            roman[i++] = 'v';
        for (; number >= 1; number -= 1)
            roman[i++] = 'i';
        return new String(roman, 0, i);
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
