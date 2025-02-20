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

        ArrayList<Long> deepest_level = new ArrayList<Long>();
        // Create a char stream.
        CharStream cs = CharStreams.fromString(paren_string);
        // Create a lexer that feeds off of the char stream.
        NestedParensLexer lexer = new NestedParensLexer(cs);
        // Create a buffer that stores all of the tokens.
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        // Create a parser that feeds off the token buffer.
        NestedParensParser parser = new NestedParensParser(tokens);
        // Begin parsing at the root rule.
        NestedParensParser.NestedParensContext tree = parser.nestedParens();
        // Walk the tree.
        ParseTreeWalker walker = new ParseTreeWalker();
        // Create a listener to traverse the parse tree.
        NestedParensListener listener = new NestedParensListener(deepest_level);
        walker.walk(listener, tree);
        return deepest_level;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
