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

        long thousand = 1000l;
        long fiveHundred = 500l;
        long oneHundred = 100l;
        long fifty = 50l;
        long ten = 10l;
        long five = 5l;
        long one = 1l;
        String[] roman = new String[20];
        roman[0] = "m";
        roman[1] = "cm";
        roman[2] = "d";
        roman[3] = "cd";
        roman[4] = "c";
        roman[5] = "xc";
        roman[6] = "lx";
        roman[7] = "xl";
        roman[8] = "x";
        roman[9] = "ix";
        roman[10] = "v";
        roman[11] = "iv";
        roman[12] = "i";
        roman[13] = "vi";
        roman[14] = "vii";
        roman[15] = "viii";
        roman[16] = "ix";
        roman[17] = "x";
        roman[18] = "xi";
        roman[19] = "xii";
        String miniRoman = "";
        int i;
        if (number >= thousand) {
            i = (int) (number / thousand);
            miniRoman = roman[0] + miniRoman;
            number = number % thousand;
        }
        if (number >= fiveHundred) {
            i = (int) (number / fiveHundred);
            miniRoman = roman[1] + miniRoman;
            number = number % fiveHundred;
        }
        if (number >= oneHundred) {
            i = (int) (number / oneHundred);
            miniRoman = roman[2] + miniRoman;
            number = number % oneHundred;
        }
        if (number >= fifty) {
            i = (int) (number / fifty);
            miniRoman = roman[3] + miniRoman;
            number = number % fifty;
        }
        if (number >= ten) {
            i = (int) (number / ten);
            miniRoman = roman[4] + miniRoman;
            number = number % ten;
        }
        if (number >= five) {
            i = (int) (number / five);
            miniRoman = roman[5] + miniRoman;
            number = number % five;
        }
        if (number >= one) {
            i = (int) (number / one);
            miniRoman = roman[6] + miniRoman;
            number = number % one;
        }
        return miniRoman;
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
