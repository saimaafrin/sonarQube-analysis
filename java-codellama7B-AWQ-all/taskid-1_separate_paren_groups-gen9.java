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

        // Write your code here.
        // Explanation
        // Your function should return a list of strings, where each string is a balanced parenthetical group from the input string.
        // The return value should be an empty list if the input string contains only unbalanced parentheses.
        // You can use any data structure you want, but it will be judged based on performance on large input strings.
        // If you want to create a list that will hold strings, you will have to explicitly declare an ArrayList of Strings.
        ArrayList<String> groupList = new ArrayList<String>();
        // Declare a stack that will hold the opening and closing parentheses.
        Stack<Character> stack = new Stack<Character>();
        // For each character in the input string.
        for (int i = 0; i < paren_string.length(); i++) {
            // If the character is an opening parenthesis.
            if (paren_string.charAt(i) == '(') {
                // Push it onto the stack.
                stack.push(paren_string.charAt(i));
            }
            // If it is a closing parenthesis.
            else if (paren_string.charAt(i) == ')') {
                // If the stack is empty, return the empty list.
                if (stack.isEmpty()) {
                    return new ArrayList<String>();
                }
                // Pop the last parenthesis from the stack.
                Character lastParenthesis = stack.pop();
                // If it is not an opening parenthesis, return the empty list.
                if (lastParenthesis != '(') {
                    return new ArrayList<String>();
                }
                // If the stack is not empty, push the last parenthesis onto the stack.
                if (!stack.isEmpty()) {
                    stack.push(lastParenthesis);
                }
            }
        }
        // If the stack is not empty, return the empty list.
        if (!stack.isEmpty()) {
            return new ArrayList<String>();
        }
        // Return the list of group strings.
        return groupList;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
