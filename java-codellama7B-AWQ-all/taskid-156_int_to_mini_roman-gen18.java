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

        String[] roman = new String[4];
        roman[0] = "m";
        roman[1] = "d";
        roman[2] = "c";
        roman[3] = "x";
        String[] ints = new String[4];
        ints[0] = "1000";
        ints[1] = "500";
        ints[2] = "100";
        ints[3] = "10";
        String[] values = new String[4];
        values[0] = "9";
        values[1] = "5";
        values[2] = "4";
        values[3] = "1";
        int[] romanNum = new int[4];
        int i = 0;
        while(number > 0){
            String intStr = String.valueOf(number%10);
            if(intStr.equals(values[i])){
                number = number/10;
                roman[i] = roman[i] + ints[i];
            }
            else if(intStr.equals("4")){
                roman[i] = roman[i] + "iv";
                number = number/10;
            }
            else if(intStr.equals("5")){
                roman[i] = roman[i] + "v";
                number = number/10;
            }
            else if(intStr.equals("9")){
                roman[i] = roman[i] + "ix";
                number = number/10;
            }
            else if(intStr.equals("4")){
                roman[i] = roman[i] + "xl";
                number = number/10;
            }
            else if(intStr.equals("9")){
                roman[i] = roman[i] + "xc";
                number = number/10;
            }
            else if(intStr.equals("4")){
                roman[i] = roman[i] + "xv";
                number = number/10;
            }
            else if(intStr.equals("9")){
                roman[i] = roman[i] + "xix";
                number = number/10;
            }
            i++;
        }
        for(int j = 0; j < 4; j++){
            if(roman[j].length() != 0){
                return roman[j];
            }
        }
        return "";
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
