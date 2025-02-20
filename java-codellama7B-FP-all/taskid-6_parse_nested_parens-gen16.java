import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    // For each of the group, output the deepest level of nesting of parentheses.
    // E.g. (()()) has maximum two levels of nesting while ((())) has three.
    // >>> parseNestedParens(("(()()) ((())) () ((())()())"))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))
    public static ArrayList<Long> parseNestedParens(String paren_string) {

        ArrayList<Long> result = new ArrayList<Long>();
        // Make a stack to store the level of nesting.
        Stack<Long> level = new Stack<Long>();
        level.push((long)0);
        // Iterate through each character in the input string.
        for (int i = 0; i < paren_string.length(); i++) {
            // If we encounter an opening parenthesis, push the current level of nesting onto the stack.
            if (paren_string.charAt(i) == '(') {
                level.push(level.peek());
            }
            // If we encounter a closing parenthesis, pop the current level of nesting from the stack.
            else if (paren_string.charAt(i) == ')') {
                level.pop();
            }
        }
        // Output the maximum level of nesting in each group of parentheses.
        for (int i = 0; i < level.size(); i++) {
            result.add(level.get(i));
        }
        return result;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
