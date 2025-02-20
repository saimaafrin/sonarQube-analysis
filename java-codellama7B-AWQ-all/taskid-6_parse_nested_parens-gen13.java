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

        // Initialize a list of deepest nesting levels.
        ArrayList<Long> max_nest = new ArrayList<>();
        // If input is empty string, return empty list.
        if(paren_string.isEmpty()) {
            return max_nest;
        }
        // Loop through each nested parentheses group.
        int j = 0;
        for(int i = 0; i < paren_string.length(); i++) {
            // If the character is opening parenthesis, increment nesting level.
            if(paren_string.charAt(i) == '(') {
                j++;
            // If the character is closing parenthesis, decrement nesting level.
            } else if(paren_string.charAt(i) == ')') {
                j--;
            }
            // If the character is the last character in the string, set the deepest nesting level.
            if(i == paren_string.length()-1) {
                max_nest.add((long)j);
            }
        }
        return max_nest;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
