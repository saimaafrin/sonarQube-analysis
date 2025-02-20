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

        long[] max_per_level = new long[1];
        long[] max_per_group = new long[1];
        Stack<Long> level_stack = new Stack<Long>();
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                level_stack.push(1l);
            } else {
                long new_level = (long) 1 + (long) level_stack.pop();
                level_stack.push(new_level);
                if (max_per_group[0] < new_level) {
                    max_per_group[0] = new_level;
                }
            }
            if (max_per_level[0] < level_stack.peek()) {
                max_per_level[0] = level_stack.peek();
            }
        }
        return new ArrayList<Long>(Arrays.asList(max_per_group[0], max_per_level[0]));
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
