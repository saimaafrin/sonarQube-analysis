import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function that takes a string as input which contains only square brackets.
    // The function should return true if and only if there is a valid subsequence of brackets 
    // where at least one bracket in the subsequence is nested.
    // >>> isNested(("[[]]"))
    // (true)
    // >>> isNested(("[]]]]]]][[[[[]"))
    // (false)
    // >>> isNested(("[][]"))
    // (false)
    // >>> isNested(("[]"))
    // (false)
    // >>> isNested(("[[][]]"))
    // (true)
    // >>> isNested(("[[]][["))
    // (true)
    public static boolean isNested(String string) {

        // Stack of characters
        Deque<Character> stack = new ArrayDeque<>();
        // Iterate through all the characters
        for (char character : string.toCharArray()) {
            // If we encounter an opening bracket
            if (character == '[') {
                // Add it to the stack
                stack.push(character);
            }
            // If we encounter a closing bracket
            else if (character == ']') {
                // If the stack is empty
                if (stack.isEmpty()) {
                    // The stack is empty, this is not a nested sequence
                    return false;
                }
                // Get the top character from the stack
                Character top = stack.peek();
                // If the top character is an opening bracket
                if (top == '[') {
                    // Remove the top character from the stack
                    stack.pop();
                } else {
                    // If the top character is a closing bracket
                    // This is a nested sequence
                    return true;
                }
            }
        }
        // If the stack is not empty, there is at least one nested bracket
        return !stack.isEmpty();
    }
    public static void main(String[] args) {
    assert(isNested(("[[]]")) == (true));
    assert(isNested(("[]]]]]]][[[[[]")) == (false));
    assert(isNested(("[][]")) == (false));
    assert(isNested(("[]")) == (false));
    assert(isNested(("[[[[]]]]")) == (true));
    assert(isNested(("[]]]]]]]]]]")) == (false));
    assert(isNested(("[][][[]]")) == (true));
    assert(isNested(("[[]")) == (false));
    assert(isNested(("[]]")) == (false));
    assert(isNested(("[[]][[")) == (true));
    assert(isNested(("[[][]]")) == (true));
    assert(isNested(("")) == (false));
    assert(isNested(("[[[[[[[[")) == (false));
    assert(isNested(("]]]]]]]]")) == (false));
    }

}
