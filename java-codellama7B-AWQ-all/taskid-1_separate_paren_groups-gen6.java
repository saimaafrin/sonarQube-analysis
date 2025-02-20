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

        // You can use a stack here
        // and a stack to keep track of opening parenthesis,
        // and a stack to keep track of closing parenthesis.
        // As you iterate over the input string, keep pushing opening parenthesis
        // into the opening_stack and closing parenthesis into the closing_stack.
        // You need to make sure that you can distinguish between closing a parenthesis
        // from the opening_stack and closing a parenthesis from the closing_stack.
        // When you encounter a closing parenthesis, you need to pop the opening parenthesis from
        // the opening_stack, and push the parenthesis in between into the result_list.
        // As you iterate through the entire input string, at the end of the string,
        // if there are still opening parenthesis in the opening_stack,
        // you need to push them into the result_list too.
        //
        // >>> Problem.separateParenGroups("((a) (b))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a)", (String)"(b)"))) ]
        // >>> Problem.separateParenGroups("((a(b)c) (d(e)f))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a(b)c)", (String)"(d(e)f)"))) ]
        // >>> Problem.separateParenGroups("((a) (b) (c))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a)", (String)"(b)", (String)"(c)"))) ]
        // >>> Problem.separateParenGroups("((a(b(c)d)e(f)g) (h(i(j)k)l) (m(n(o)p)q))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a(b(c)d)e(f)g)", (String)"(h(i(j)k)l)", (String)"(m(n(o)p)q)"))) ]
        // >>> Problem.separateParenGroups("((a(b)c(d)e) (f(g(h)i)j) (k(l(m)n)o))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a(b)c(d)e)", (String)"(f(g(h)i)j)", (String)"(k(l(m)n)o)"))) ]
        // >>> Problem.separateParenGroups("((a) (b) (c) (d) (e))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a)", (String)"(b)", (String)"(c)", (String)"(d)", (String)"(e)"))) ]
        // >>> Problem.separateParenGroups("((a(b)c) (d(e)f) (g(h)i))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a(b)c)", (String)"(d(e)f)", (String)"(g(h)i)"))) ]
        // >>> Problem.separateParenGroups("((a(b)c(d)e(f)) (g(h)i(j)k) (l(m(n)o)p))")
        // [ (new ArrayList<String>(Arrays.asList((String)"(a(b
    }
    public static void main(String[] args) {
    assert(separateParenGroups(("(()()) ((())) () ((())()())")).equals((new ArrayList<String>(Arrays.asList((String)"(()())", (String)"((()))", (String)"()", (String)"((())()())")))));
    assert(separateParenGroups(("() (()) ((())) (((())))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"((()))", (String)"(((())))")))));
    assert(separateParenGroups(("(()(())((())))")).equals((new ArrayList<String>(Arrays.asList((String)"(()(())((())))")))));
    assert(separateParenGroups(("( ) (( )) (( )( ))")).equals((new ArrayList<String>(Arrays.asList((String)"()", (String)"(())", (String)"(()())")))));
    }

}
