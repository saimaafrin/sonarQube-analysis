import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
    // >>> cycpatternCheck(("abcd"), ("abd"))
    // (false)
    // >>> cycpatternCheck(("hello"), ("ell"))
    // (true)
    // >>> cycpatternCheck(("whassup"), ("psus"))
    // (false)
    // >>> cycpatternCheck(("abab"), ("baa"))
    // (true)
    // >>> cycpatternCheck(("efef"), ("eeff"))
    // (false)
    // >>> cycpatternCheck(("himenss"), ("simen"))
    // (true)
    public static boolean cycpatternCheck(String a, String b) {

        // return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1));
        // return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1)) || isSubstring(a,b.substring(2) + b.substring(0,2));
        // return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1)) || isSubstring(a,b.substring(2) + b.substring(0,2)) || isSubstring(a,b.substring(3) + b.substring(0,3));
        // return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1)) || isSubstring(a,b.substring(2) + b.substring(0,2)) || isSubstring(a,b.substring(3) + b.substring(0,3)) || isSubstring(a,b.substring(4) + b.substring(0,4));
        // return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1)) || isSubstring(a,b.substring(2) + b.substring(0,2)) || isSubstring(a,b.substring(3) + b.substring(0,3)) || isSubstring(a,b.substring(4) + b.substring(0,4)) || isSubstring(a,b.substring(5) + b.substring(0,5));
        return isSubstring(a,b) || isSubstring(a,b.substring(1) + b.substring(0,1)) || isSubstring(a,b.substring(2) + b.substring(0,2)) || isSubstring(a,b.substring(3) + b.substring(0,3)) || isSubstring(a,b.substring(4) + b.substring(0,4)) || isSubstring(a,b.substring(5) + b.substring(0,5)) || isSubstring(a,b.substring(6) + b.substring(0,6));
    }
    public static void main(String[] args) {
    assert(cycpatternCheck(("xyzw"), ("xyw")) == (false));
    assert(cycpatternCheck(("yello"), ("ell")) == (true));
    assert(cycpatternCheck(("whattup"), ("ptut")) == (false));
    assert(cycpatternCheck(("efef"), ("fee")) == (true));
    assert(cycpatternCheck(("abab"), ("aabb")) == (false));
    assert(cycpatternCheck(("winemtt"), ("tinem")) == (true));
    }

}
