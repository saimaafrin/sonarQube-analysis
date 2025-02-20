import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input are two strings a and b consisting only of 1s and 0s.
    // Perform binary XOR on these inputs and return result also as a string.
    // >>> stringXor(("010"), ("110"))
    // ("100")
    public static String stringXor(String a, String b) {

        if(a.length()!=b.length()){
            return "0";
        }
        String result="";
        for(int i=0; i<a.length(); i++){
            if(a.charAt(i)==b.charAt(i)){
                result+=a.charAt(i);
            }
            else{
                result+=(a.charAt(i)=='0'&&b.charAt(i)=='1'?"1":"0");
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(stringXor(("111000"), ("101010")).equals(("010010")));
    assert(stringXor(("1"), ("1")).equals(("0")));
    assert(stringXor(("0101"), ("0000")).equals(("0101")));
    }

}
