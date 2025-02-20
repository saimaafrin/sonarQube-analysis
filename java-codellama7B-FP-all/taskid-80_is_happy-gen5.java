import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a string s.
    // Your task is to check if the string is hapjava or not.
    // A string is hapjava if its length is at least 3 and every 3 consecutive letters are distinct
    // For example:
    // >>> isHappy(("a"))
    // (false)
    // >>> isHappy(("aa"))
    // (false)
    // >>> isHappy(("abcd"))
    // (true)
    // >>> isHappy(("aabb"))
    // (false)
    // >>> isHappy(("adb"))
    // (true)
    // >>> isHappy(("xyy"))
    // (false)
    public static boolean isHappy(String s) {

        if(s.length()<3) return false;
        boolean[] seen = new boolean[s.length()];
        for(int i=0; i<s.length(); i+=3){
            String substring = s.substring(i,i+3);
            if(seen[i/3]) return false;
            for(int j=0; j<substring.length(); j++){
                if(substring.charAt(j)=='a' || substring.charAt(j)=='b' || substring.charAt(j)=='c'){
                    if(substring.charAt(j)=='a' && i/3==2){
                        seen[i/3] = true;
                    }else if(substring.charAt(j)=='b' && i/3==1){
                        seen[i/3] = true;
                    }else if(substring.charAt(j)=='c' && i/3==0){
                        seen[i/3] = true;
                    }
                }
            }
        }
        return true;
    }
    public static void main(String[] args) {
    assert(isHappy(("a")) == (false));
    assert(isHappy(("aa")) == (false));
    assert(isHappy(("abcd")) == (true));
    assert(isHappy(("aabb")) == (false));
    assert(isHappy(("adb")) == (true));
    assert(isHappy(("xyy")) == (false));
    assert(isHappy(("iopaxpoi")) == (true));
    assert(isHappy(("iopaxioi")) == (false));
    }

}
