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

        Stack<Character> paren_stack = new Stack<Character>();
        StringBuilder current_group = new StringBuilder();
        ArrayList<String> group_list = new ArrayList<String>();
        for (int i = 0; i < paren_string.length(); i++) {
            char paren = paren_string.charAt(i);
            if (paren == '(') {
                paren_stack.push(paren);
            } else if (paren == ')') {
                if (!paren_stack.empty()) {
                    paren_stack.pop();
                } else {
                    current_group.append(paren);
                }
            } else {
                current_group.append(paren);
            }
        }
        if (paren_stack.empty()) {
            group_list.add(current_group.toString());
        } else {
            group_list.add(current_group.toString());
            String rest = paren_string.substring(paren_string.length() - paren_stack.size());
            group_list.addAll(separateParenGroups(rest));
        }
        return group_list;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
