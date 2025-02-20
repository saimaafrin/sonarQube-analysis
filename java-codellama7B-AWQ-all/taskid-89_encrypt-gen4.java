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

        char[] array = s.toCharArray();
        char[] result = new char[array.length];
        int j = 0;
        for(int i = 0; i < array.length; i++){
            if(array[i] == 'a'){
                result[j] = 'c';
                j++;
            } else if(array[i] == 'b'){
                result[j] = 'd';
                j++;
            } else if(array[i] == 'c'){
                result[j] = 'e';
                j++;
            } else if(array[i] == 'd'){
                result[j] = 'f';
                j++;
            } else if(array[i] == 'e'){
                result[j] = 'g';
                j++;
            } else if(array[i] == 'f'){
                result[j] = 'h';
                j++;
            } else if(array[i] == 'g'){
                result[j] = 'i';
                j++;
            } else if(array[i] == 'h'){
                result[j] = 'j';
                j++;
            } else if(array[i] == 'i'){
                result[j] = 'k';
                j++;
            } else if(array[i] == 'j'){
                result[j] = 'l';
                j++;
            } else if(array[i] == 'k'){
                result[j] = 'm';
                j++;
            } else if(array[i] == 'l'){
                result[j] = 'n';
                j++;
            } else if(array[i] == 'm'){
                result[j] = 'o';
                j++;
            } else if(array[i] == 'n'){
                result[j] = 'p';
                j++;
            } else if(array[i] == 'o'){
                result[j] = 'q';
                j++;
            } else if(array[i] == 'p'){
                result[j] = 'r';
                j++;
            } else if(array[i] == 'q'){
                result[j] = 's';
                j++;
            } else if(array[i] == 'r'){
                result[j] = 't';
                j++;
            } else if(array[i] == 's'){
                result[j] = 'u';
                j++;
            } else if(array[i] == 't'){
                result[j] = 'v';
                j++;
            } else if(array[i] == 'u'){
                result[j] = 'w';
                j++;
            } else if(array[i] == 'v'){
                result[j] = 'x';
                j++;
            } else if(array[i] == 'w'){
                result[j] = 'y';
                j++;
            } else if(array[i] == 'x'){
                result[j] = 'z';
                j++;
            } else if(array[i] == 'y'){
                result[j] = 'a';
                j++;
            } else if(array[i] == 'z'){
                result[j] = 'b';
                j++;
            }
        }
        return new String(result);
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
