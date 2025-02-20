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

        String newS = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            newS += c;
        }
        newS = newS.toUpperCase();
        for (int i = 0; i < newS.length(); i++) {
            char c = newS.charAt(i);
            if (c == 'A' || c == 'B' || c == 'C') {
                newS = newS.replace("A", "C");
                newS = newS.replace("B", "A");
                newS = newS.replace("C", "B");
            } else if (c == 'D' || c == 'E' || c == 'F') {
                newS = newS.replace("D", "F");
                newS = newS.replace("E", "D");
                newS = newS.replace("F", "E");
            } else if (c == 'G' || c == 'H' || c == 'I') {
                newS = newS.replace("G", "I");
                newS = newS.replace("H", "G");
                newS = newS.replace("I", "H");
            } else if (c == 'J' || c == 'K' || c == 'L') {
                newS = newS.replace("J", "L");
                newS = newS.replace("K", "J");
                newS = newS.replace("L", "K");
            } else if (c == 'M' || c == 'N' || c == 'O') {
                newS = newS.replace("M", "O");
                newS = newS.replace("N", "M");
                newS = newS.replace("O", "N");
            } else if (c == 'P' || c == 'Q' || c == 'R') {
                newS = newS.replace("P", "R");
                newS = newS.replace("Q", "P");
                newS = newS.replace("R", "Q");
            } else if (c == 'S' || c == 'T' || c == 'U') {
                newS = newS.replace("S", "U");
                newS = newS.replace("T", "S");
                newS = newS.replace("U", "T");
            } else if (c == 'V' || c == 'W' || c == 'X') {
                newS = newS.replace("V", "X");
                newS = newS.replace("W", "V");
                newS = newS.replace("X", "W");
            } else if (c == 'Y' || c == 'Z' || c == 'A') {
                newS = newS.replace("Y", "A");
                newS = newS.replace("Z", "Y");
                newS = newS.replace("A", "Z");
            }
        }
        return newS;
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
