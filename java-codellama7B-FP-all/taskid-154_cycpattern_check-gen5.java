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

        if(b.length()==0) return false;
        // for(int i=0;i<a.length();i++){
        //     for(int j=1;j<=b.length();j++){
        //         if(a.substring(i,i+j).equals(b)){
        //             return true;
        //         }
        //     }
        // }
        return a.contains(b)||a.contains(rotate(b,1))||a.contains(rotate(b,2))||a.contains(rotate(b,3))||a.contains(rotate(b,4))||a.contains(rotate(b,5))||a.contains(rotate(b,6))||a.contains(rotate(b,7))||a.contains(rotate(b,8))||a.contains(rotate(b,9))||a.contains(rotate(b,10))||a.contains(rotate(b,11))||a.contains(rotate(b,12))||a.contains(rotate(b,13))||a.contains(rotate(b,14))||a.contains(rotate(b,15));
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
