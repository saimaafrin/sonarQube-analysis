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

        ArrayList<Long> res = new ArrayList<Long>();
        // split string on spaces
        String[] paren_groups = paren_string.split("\\s+");
        // loop through each group
        for (String paren_group : paren_groups) {
            // create stack to track depth of nesting
            Stack<Character> paren_stack = new Stack<Character>();
            // for each char in group
            for (char c : paren_group.toCharArray()) {
                // if left paren, add it to stack
                if (c == '(') paren_stack.add(c);
                // if right paren, check if stack is empty
                if (c == ')') {
                    if (paren_stack.empty())
                        throw new IllegalArgumentException("Mismatched parentheses.");
                    // if not empty, pop stack
                    paren_stack.pop();
                }
            }
            // if stack not empty, throw exception
            if (!paren_stack.empty())
                throw new IllegalArgumentException("Mismatched parentheses.");
            // push depth of nesting to results list
            res.add((long) paren_stack.size());
        }
        return res;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
