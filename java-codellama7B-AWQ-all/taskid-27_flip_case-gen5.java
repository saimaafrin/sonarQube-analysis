import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    // >>> flipCase(("Hello"))
    // ("hELLO")
    public static String flipCase(String string) {

        char[] str = string.toCharArray();
        String caseFlipped = "";
        for (char c : str) {
            if (Character.isUpperCase(c)) {
                caseFlipped += Character.toLowerCase(c);
            } else if (Character.isLowerCase(c)) {
                caseFlipped += Character.toUpperCase(c);
            } else {
                caseFlipped += c;
            }
        }
        return caseFlipped;
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
