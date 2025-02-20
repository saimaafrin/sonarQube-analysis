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

        // Write your code here
        Stack<Integer> stack = new Stack<Integer>();
        int level = 0;
        ArrayList<Long> result = new ArrayList<>();
        for (int i = 0; i < paren_string.length(); i++) {
            char ch = paren_string.charAt(i);
            if (ch == '(') {
                stack.push(level);
                level++;
            } else if (ch == ')') {
                level = stack.pop();
            }
        }
        for (int i = 0; i < paren_string.length(); i++) {
            char ch = paren_string.charAt(i);
            if (ch == '(') {
                result.add((long)level);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
