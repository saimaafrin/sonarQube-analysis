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

        char[] c = s.toCharArray();
        for (int i = 0; i < c.length; i++) {
            if (c[i] == ' ') {
                continue;
            }
            if (c[i] == 'a') {
                c[i] = 'e';
                continue;
            }
            if (c[i] == 'b') {
                c[i] = 'f';
                continue;
            }
            if (c[i] == 'c') {
                c[i] = 'g';
                continue;
            }
            if (c[i] == 'd') {
                c[i] = 'h';
                continue;
            }
            if (c[i] == 'e') {
                c[i] = 'i';
                continue;
            }
            if (c[i] == 'f') {
                c[i] = 'j';
                continue;
            }
            if (c[i] == 'g') {
                c[i] = 'k';
                continue;
            }
            if (c[i] == 'h') {
                c[i] = 'l';
                continue;
            }
            if (c[i] == 'i') {
                c[i] = 'm';
                continue;
            }
            if (c[i] == 'j') {
                c[i] = 'n';
                continue;
            }
            if (c[i] == 'k') {
                c[i] = 'o';
                continue;
            }
            if (c[i] == 'l') {
                c[i] = 'p';
                continue;
            }
            if (c[i] == 'm') {
                c[i] = 'q';
                continue;
            }
            if (c[i] == 'n') {
                c[i] = 'r';
                continue;
            }
            if (c[i] == 'o') {
                c[i] = 's';
                continue;
            }
            if (c[i] == 'p') {
                c[i] = 't';
                continue;
            }
            if (c[i] == 'q') {
                c[i] = 'u';
                continue;
            }
            if (c[i] == 'r') {
                c[i] = 'v';
                continue;
            }
            if (c[i] == 's') {
                c[i] = 'w';
                continue;
            }
            if (c[i] == 't') {
                c[i] = 'x';
                continue;
            }
            if (c[i] == 'u') {
                c[i] = 'y';
                continue;
            }
            if (c[i] == 'v') {
                c[i] = 'z';
                continue;
            }
            if (c[i] == 'w') {
                c[i] = 'a';
                continue;
            }
            if (c[i] == 'x') {
                c[i] = 'b';
                continue;
            }
            if (c[i] == 'y') {
                c[i] = 'c';
                continue;
            }
            if (c[i] == 'z') {
                c[i] = 'd';
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
