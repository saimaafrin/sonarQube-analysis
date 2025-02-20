import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    // separate those group into separate strings and return the array list of those.
    // Separate groups are balanced (each open brace is properly closed) and not nested within each other
    // Ignore any spaces in the input string.
    // >>> separateParenGroups(("( ) (( )) (( )( ))"))
    // (new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))
    public static ArrayList<String> separateParenGroups(String paren_string) {

        int count = 0;
        ArrayList<String> result = new ArrayList<String>();
        int i = 0;
        while (i < paren_string.length()) {
            if (paren_string.charAt(i) == '(') {
                count++;
            } else if (paren_string.charAt(i) == ')') {
                count--;
            }
            i++;
        }
        int start = 0;
        for (i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                if (count == 0) {
                    result.add(paren_string.substring(start, i));
                    start = i + 1;
                }
                count++;
            } else if (paren_string.charAt(i) == ')') {
                count--;
                if (count == 0) {
                    result.add(paren_string.substring(start, i + 1));
                    start = i + 1;
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
