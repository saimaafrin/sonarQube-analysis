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

        ArrayList<String> paren_groups = new ArrayList<String>();
        // Find the positions of all the opening parentheses.
        ArrayList<Integer> op = new ArrayList<Integer>();
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                op.add(i);
            }
        }
        // Find the positions of all the closing parentheses.
        ArrayList<Integer> cp = new ArrayList<Integer>();
        for (int i = paren_string.length() - 1; i >= 0; i--) {
            if (paren_string.charAt(i) == ')') {
                cp.add(i);
            }
        }
        // Make sure that the number of opening and closing parentheses are equal.
        assert op.size() == cp.size();
        for (int i = 0; i < op.size(); i++) {
            // We will only be looking at a group if the opening and closing parentheses are together in the input.
            if (i < op.size() - 1 && cp.get(i) == op.get(i) + 1 && cp.get(i + 1) == op.get(i) + 2) {
                String group = paren_string.substring(op.get(i) + 1, cp.get(i) - 1);
                paren_groups.add(group);
            }
        }
        return paren_groups;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
