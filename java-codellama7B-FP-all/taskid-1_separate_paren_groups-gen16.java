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

        ArrayList<String> group_list = new ArrayList<String>();
        int curr_group_start = 0;
        int curr_group_end = 0;
        int curr_group_size = 0;
        boolean still_open = false;
        char curr_char = ' ';
        for (int i = 0; i < paren_string.length(); i++) {
            curr_char = paren_string.charAt(i);
            if (curr_char == '(') {
                still_open = true;
                curr_group_start = i;
            } else if (curr_char == ')') {
                still_open = false;
                curr_group_end = i;
                curr_group_size = curr_group_end - curr_group_start + 1;
                String new_group = paren_string.substring(curr_group_start, curr_group_end + 1);
                group_list.add(new_group);
            }
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
