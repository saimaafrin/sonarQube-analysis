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

        ArrayList<Long> ans = new ArrayList<>();
        for (String paren : paren_string.split(" ")) {
            // Each group is represented as a string of parens.
            long nest_level = 0;
            // Set the nest level to the first paren.
            // If the first paren is an open paren, then the nest level will increase.
            // If the first paren is a close paren, then the nest level will decrease.
            // Thus, the nest level is the maximum of the number of open parens and the number of close parens.
            char first_paren = paren.charAt(0);
            char last_paren = paren.charAt(paren.length() - 1);
            if (first_paren == '(') {
                nest_level = 1;
            }
            if (last_paren == ')') {
                nest_level = 1;
            }
            // Iterate over each char in the group.
            for (int i = 1; i < paren.length() - 1; i++) {
                char c = paren.charAt(i);
                if (c == '(') {
                    nest_level++;
                }
                if (c == ')') {
                    nest_level--;
                }
            }
            // Store the maximum of the nest level and the answer.
            ans.add((long) Math.max(nest_level, ans.get(ans.size() - 1)));
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
