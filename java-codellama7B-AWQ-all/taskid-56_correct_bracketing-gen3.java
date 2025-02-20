import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // brackets is a string of "<" and ">".
    // return true if every opening bracket has a corresponding closing bracket.
    // >>> correctBracketing(("<"))
    // (false)
    // >>> correctBracketing(("<>"))
    // (true)
    // >>> correctBracketing(("<<><>>"))
    // (true)
    // >>> correctBracketing(("><<>"))
    // (false)
    public static boolean correctBracketing(String brackets) {

        // This is a "method-only" submission.
        // You only need to write a method for this problem and
        // use the following function signature (ignoring
        // return type and parameters names).
        // stack is a stack of chars that we are using to
        // keep track of the opening brackets.
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < brackets.length(); i++) {
            // if we have an opening bracket
            if (brackets.charAt(i) == '<') {
                // we add it to the stack.
                stack.push('<');
            } else if (brackets.charAt(i) == '>') {
                // if we have a closing bracket
                // and the stack is not empty
                // and the last opening bracket on the
                // stack is the same as this closing bracket
                // we pop it from the stack.
                if (!stack.isEmpty() && stack.peek() == '<') {
                    stack.pop();
                } else {
                    // otherwise
                    // we return false
                    return false;
                }
            }
        }
        // finally if the stack is empty
        // we return true
        return stack.isEmpty();
    }
    public static void main(String[] args) {
    assert(correctBracketing(("<>")) == (true));
    assert(correctBracketing(("<<><>>")) == (true));
    assert(correctBracketing(("<><><<><>><>")) == (true));
    assert(correctBracketing(("<><><<<><><>><>><<><><<>>>")) == (true));
    assert(correctBracketing(("<<<><>>>>")) == (false));
    assert(correctBracketing(("><<>")) == (false));
    assert(correctBracketing(("<")) == (false));
    assert(correctBracketing(("<<<<")) == (false));
    assert(correctBracketing((">")) == (false));
    assert(correctBracketing(("<<>")) == (false));
    assert(correctBracketing(("<><><<><>><>><<>")) == (false));
    assert(correctBracketing(("<><><<><>><>>><>")) == (false));
    }

}
