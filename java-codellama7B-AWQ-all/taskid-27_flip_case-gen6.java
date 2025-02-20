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

        String[] arrayOfStrings = string.split("");
        StringBuffer buffer = new StringBuffer();
        for (String s : arrayOfStrings) {
            if (s.equals(s.toLowerCase())) {
                buffer.append(s.toUpperCase());
            } else {
                buffer.append(s.toLowerCase());
            }
        }
        return buffer.toString();
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
