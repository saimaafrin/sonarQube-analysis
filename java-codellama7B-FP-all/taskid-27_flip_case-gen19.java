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

        String temp = "";
        for(int i = 0; i < string.length(); i++){
            if(Character.isLowerCase(string.charAt(i))){
                temp += Character.toUpperCase(string.charAt(i));
            }
            else if(Character.isUpperCase(string.charAt(i))){
                temp += Character.toLowerCase(string.charAt(i));
            }
            else{
                temp += string.charAt(i);
            }
        }
        return temp;
    }
    public static void main(String[] args) {
    assert(flipCase(("")).equals(("")));
    assert(flipCase(("Hello!")).equals(("hELLO!")));
    assert(flipCase(("These violent delights have violent ends")).equals(("tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS")));
    }

}
