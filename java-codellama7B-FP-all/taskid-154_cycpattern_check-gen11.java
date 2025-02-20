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

        // return a.contains(b) || a.contains(b.substring(1) + b.charAt(0)) || a.contains(b.substring(2) + b.charAt(0) + b.charAt(1)) || a.contains(b.substring(3) + b.charAt(0) + b.charAt(1) + b.charAt(2)) || a.contains(b.substring(4) + b.charAt(0) + b.charAt(1) + b.charAt(2) + b.charAt(3));
        String cycB = b;
        while (cycB.length() < a.length()) cycB += b;
        if (a.contains(cycB) || a.contains(cycB.substring(1) + cycB.charAt(0))) return true;
        if (cycB.length() > 2) {
            cycB = cycB.substring(1) + cycB.charAt(0);
            if (a.contains(cycB) || a.contains(cycB.substring(1) + cycB.charAt(0))) return true;
            if (cycB.length() > 3) {
                cycB = cycB.substring(1) + cycB.charAt(0);
                if (a.contains(cycB) || a.contains(cycB.substring(1) + cycB.charAt(0))) return true;
                if (cycB.length() > 4) {
                    cycB = cycB.substring(1) + cycB.charAt(0);
                    if (a.contains(cycB) || a.contains(cycB.substring(1) + cycB.charAt(0))) return true;
                    if (cycB.length() > 5) {
                        cycB = cycB.substring(1) + cycB.charAt(0);
                        if (a.contains(cycB) || a.contains(cycB.substring(1) + cycB.charAt(0))) return true;
                    }
                }
            }
        }
        return false;
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
