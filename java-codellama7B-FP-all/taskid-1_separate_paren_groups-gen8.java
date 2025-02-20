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

        ArrayList<String> groups = new ArrayList<>();
        StringBuilder current_group = new StringBuilder();
        char open_bracket = '(';
        char close_bracket = ')';
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == open_bracket) {
                current_group.append(open_bracket);
            } else if (paren_string.charAt(i) == close_bracket) {
                current_group.append(close_bracket);
            }
            if (paren_string.charAt(i) == close_bracket && i + 1 < paren_string.length() && paren_string.charAt(i + 1) == open_bracket) {
                groups.add(current_group.toString());
                current_group = new StringBuilder();
                i++;
            }
        }
        groups.add(current_group.toString());
        return groups;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
