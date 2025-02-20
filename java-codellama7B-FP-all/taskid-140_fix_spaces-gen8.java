import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a string text, replace all spaces in it with underscores, 
    // and if a string has more than 2 consecutive spaces, 
    // then replace all consecutive spaces with - 
    // >>> fixSpaces((" Example"))
    // ("Example")
    // >>> fixSpaces((" Example 1"))
    // ("Example_1")
    // >>> fixSpaces((" Example 2"))
    // ("_Example_2")
    // >>> fixSpaces((" Example 3"))
    // ("_Example-3")
    public static String fixSpaces(String text) {

        StringBuilder fixed = new StringBuilder();
        int len = text.length();
        int currentRun = 0;
        for (int i = 0; i < len; i++) {
            if (text.charAt(i) == ' ') {
                if (currentRun == 0) {
                    currentRun = 1;
                    fixed.append("_");
                } else {
                    currentRun++;
                }
            } else {
                if (currentRun > 0) {
                    if (currentRun == 1) {
                        fixed.append(text.charAt(i));
                    } else {
                        fixed.append("-");
                    }
                    currentRun = 0;
                } else {
                    fixed.append(text.charAt(i));
                }
            }
        }
        return fixed.toString();
    }
    public static void main(String[] args) {
    assert(fixSpaces(("Example")).equals(("Example")));
    assert(fixSpaces(("Mudasir Hanif ")).equals(("Mudasir_Hanif_")));
    assert(fixSpaces(("Yellow Yellow  Dirty  Fellow")).equals(("Yellow_Yellow__Dirty__Fellow")));
    assert(fixSpaces(("Exa   mple")).equals(("Exa-mple")));
    assert(fixSpaces(("   Exa 1 2 2 mple")).equals(("-Exa_1_2_2_mple")));
    }

}
