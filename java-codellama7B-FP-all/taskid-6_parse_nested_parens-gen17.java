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

        // Initialize variables
        int num_groups = 0;
        ArrayList<Long> deepest_levels = new ArrayList<Long>();
        // The current deepest level of nesting.
        long deepest = 0;
        // The current level of nesting.
        long level = 0;
        // The index of the last open parentheses.
        int last_open = -1;
        // The index of the last close parentheses.
        int last_close = -1;
        // Parse through the string one character at a time.
        for (int i = 0; i < paren_string.length(); i++) {
            // Check if we have an opening parentheses.
            if (paren_string.charAt(i) == '(') {
                // Increase the level of nesting.
                level++;
                // If this is the deepest level of nesting so far, update deepest.
                if (level > deepest) {
                    deepest = level;
                }
                // Keep track of the last open parentheses.
                last_open = i;
            }
            // Check if we have a closing parentheses.
            if (paren_string.charAt(i) == ')') {
                // Decrease the level of nesting.
                level--;
                // If the level is now 0, we've found the deepest level of nesting for the group.
                if (level == 0) {
                    // Add the deepest level to the list of deepest levels.
                    deepest_levels.add(deepest);
                    // Reset the deepest level of nesting.
                    deepest = 0;
                }
                // Keep track of the last close parentheses.
                last_close = i;
            }
        }
        // If the string ends with an open parentheses, the deepest level of nesting is 0.
        if (last_open == paren_string.length() - 1) {
            deepest_levels.add((long) 0);
        }
        return deepest_levels;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
