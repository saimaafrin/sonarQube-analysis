import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function encrypt that takes a string as an argument and
    // returns a string encrypted with the alphabet being rotated. 
    // The alphabet should be rotated in a manner such that the letters 
    // shift down by two multiplied to two places.
    // For example:
    // >>> encrypt(("hi"))
    // ("lm")
    // >>> encrypt(("asdfghjkl"))
    // ("ewhjklnop")
    // >>> encrypt(("gf"))
    // ("kj")
    // >>> encrypt(("et"))
    // ("ix")
    public static String encrypt(String s) {

        String ret = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c < 123) {
                if (c < 91) {
                    if (c <= 77) {
                        if (c <= 69) {
                            ret += (char) (c + 2 * 2);
                        } else {
                            ret += (char) (c - 2 * 2 + 1);
                        }
                    } else {
                        ret += (char) (c - 2 * 2 + 13);
                    }
                } else {
                    if (c <= 90) {
                        ret += (char) (c + 2 * 2 - 26);
                    } else {
                        ret += (char) (c + 2 * 2);
                    }
                }
            } else {
                if (c < 123) {
                    ret += (char) (c - 2 * 2 + 128);
                } else {
                    ret += (char) (c + 2 * 2 - 26);
                }
            }
        }
        return ret;
    }
    public static void main(String[] args) {
    assert(encrypt(("hi")).equals(("lm")));
    assert(encrypt(("asdfghjkl")).equals(("ewhjklnop")));
    assert(encrypt(("gf")).equals(("kj")));
    assert(encrypt(("et")).equals(("ix")));
    assert(encrypt(("faewfawefaewg")).equals(("jeiajeaijeiak")));
    assert(encrypt(("hellomyfriend")).equals(("lippsqcjvmirh")));
    assert(encrypt(("dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh")).equals(("hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl")));
    assert(encrypt(("a")).equals(("e")));
    }

}
