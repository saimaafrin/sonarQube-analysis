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

        if (a.length() < b.length() || b.length() == 0) {
            return false;
        }
        int a_len = a.length();
        int b_len = b.length();
        int[] b_rotations = new int[b_len];
        for (int i = 0; i < b_len; i++) {
            b_rotations[i] = (b.charAt(i) + 1) % 26;
        }
        for (int i = 0; i < b_len; i++) {
            int j = 0;
            while (j < a_len) {
                if (a.charAt(j) == b.charAt(i)) {
                    int k = i;
                    boolean found = true;
                    while (k < a_len) {
                        if (a.charAt(k) == b.charAt(j)) {
                            k += 1;
                            j += 1;
                        } else {
                            k += 1;
                            if (j < b_len) {
                                j = b_rotations[j];
                            } else {
                                found = false;
                                break;
                            }
                        }
                    }
                    if (found) {
                        return true;
                    }
                }
                j += 1;
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
