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

        // Input validation
        if (paren_string == null || paren_string.length() == 0) {
            return new ArrayList<String>();
        }
        // Create a stack that will keep track of where the opening and closing parentheses are.
        // Since we don't know how many groups we'll be dealing with, we start with a small stack
        // and then we'll resize it as needed.
        Deque<Integer> braces = new ArrayDeque<Integer>(10);
        braces.push(0);
        // This is our output array
        ArrayList<String> groups = new ArrayList<String>();
        // Iterate through the input string and look for opening and closing parentheses.
        // Once we've found a pair, we'll pop the opening brace, push the closing brace, and add
        // everything in between to the output.
        for (int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                braces.push(i);
            } else if (c == ')') {
                if (braces.isEmpty()) {
                    throw new RuntimeException("Mismatched parentheses");
                }
                int start = braces.pop();
                groups.add(paren_string.substring(start + 1, i));
            }
        }
        // If there's anything left in the braces stack, it means there were more opening
        // parentheses than closing ones.
        if (!braces.isEmpty()) {
            throw new RuntimeException("Mismatched parentheses");
        }
        // Return the output array
        return groups;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
