import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Check if two words have the same characters.
    // >>> sameChars(("eabcdzzzz"), ("dddzzzzzzzddeddabc"))
    // (true)
    // >>> sameChars(("abcd"), ("dddddddabc"))
    // (true)
    // >>> sameChars(("dddddddabc"), ("abcd"))
    // (true)
    // >>> sameChars(("eabcd"), ("dddddddabc"))
    // (false)
    // >>> sameChars(("abcd"), ("dddddddabce"))
    // (false)
    // >>> sameChars(("eabcdzzzz"), ("dddzzzzzzzddddabc"))
    // (false)
    public static boolean sameChars(String s0, String s1) {

        if (s0.length() != s1.length()) return false;
        for (int i = 0; i < s0.length(); i++) if (s0.charAt(i) != s1.charAt(i)) return false;
        return true;
    }
    public static void main(String[] args) {
    assert(sameChars(("eabcdzzzz"), ("dddzzzzzzzddeddabc")) == (true));
    assert(sameChars(("abcd"), ("dddddddabc")) == (true));
    assert(sameChars(("dddddddabc"), ("abcd")) == (true));
    assert(sameChars(("eabcd"), ("dddddddabc")) == (false));
    assert(sameChars(("abcd"), ("dddddddabcf")) == (false));
    assert(sameChars(("eabcdzzzz"), ("dddzzzzzzzddddabc")) == (false));
    assert(sameChars(("aabb"), ("aaccc")) == (false));
    }

}
