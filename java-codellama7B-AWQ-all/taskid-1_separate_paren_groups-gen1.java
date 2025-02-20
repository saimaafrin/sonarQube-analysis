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

        ArrayList<String> groups = new ArrayList<String>();
        String[] tokens = paren_string.trim().split("\\s+");
        int start = 0, end = 0, cnt = 0;
        for (int i = 0; i < tokens.length; i++) {
            String token = tokens[i];
            if (token.equals("(")) {
                if (cnt == 0) start = i;
                cnt++;
            } else if (token.equals(")")) {
                if (cnt == 0) throw new RuntimeException("Closing brace without matching open brace");
                cnt--;
                if (cnt == 0) {
                    end = i;
                    groups.add(paren_string.substring(start, end + 1));
                }
            }
        }
        if (cnt > 0) throw new RuntimeException("No closing brace found");
        return groups;
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
