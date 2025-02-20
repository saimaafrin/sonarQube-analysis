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

        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < string.length(); i++) {
            if(Character.isUpperCase(string.charAt(i))) {
                sb.append(Character.toLowerCase(string.charAt(i)));
            } else {
                sb.append(Character.toUpperCase(string.charAt(i)));
            }
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
