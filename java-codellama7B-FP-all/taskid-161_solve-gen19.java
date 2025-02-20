import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a string s.
    // if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    // otherwise keep it as it is.
    // If the string contains no letters, reverse the string.
    // The function should return the resulted string.
    // Examples
    // >>> solve(("1234"))
    // ("4321")
    // >>> solve(("ab"))
    // ("AB")
    // >>> solve(("#a@C"))
    // ("#A@c")
    public static String solve(String s) {

        char[] str = s.toCharArray();
        char[] result = new char[s.length()];
        boolean containsLetter = false;
        for (int i = 0; i < str.length; i++) {
            if (str[i] >= 'a' && str[i] <= 'z') {
                containsLetter = true;
                result[i] = (char) (str[i] - 32);
            } else if (str[i] >= 'A' && str[i] <= 'Z') {
                containsLetter = true;
                result[i] = (char) (str[i] + 32);
            } else {
                result[i] = str[i];
            }
        }
        if (!containsLetter) {
            for (int i = 0; i < str.length; i++) {
                result[i] = (char) (str[i] - 32);
            }
        }
        return new String(result);
    }
    public static void main(String[] args) {
    assert(solve(("AsDf")).equals(("aSdF")));
    assert(solve(("1234")).equals(("4321")));
    assert(solve(("ab")).equals(("AB")));
    assert(solve(("#a@C")).equals(("#A@c")));
    assert(solve(("#AsdfW^45")).equals(("#aSDFw^45")));
    assert(solve(("#6@2")).equals(("2@6#")));
    assert(solve(("#$a^D")).equals(("#$A^d")));
    assert(solve(("#ccc")).equals(("#CCC")));
    }

}
