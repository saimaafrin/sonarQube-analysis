import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return length of given string
    // >>> stringLength((""))
    // (0l)
    // >>> stringLength(("abc"))
    // (3l)
    public static long strlen(String string) {

        return string.length();
    }
    public static void main(String[] args) {
    assert(strlen(("")) == (0l));
    assert(strlen(("x")) == (1l));
    assert(strlen(("asdasnakj")) == (9l));
    }

}
