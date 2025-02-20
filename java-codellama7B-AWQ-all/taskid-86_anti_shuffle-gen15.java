import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes a string and returns an ordered version of it.
    // Ordered version of string, is a string where all words (separated by space)
    // are replaced by a new word where all the characters arranged in
    // ascending order based on ascii value.
    // Note: You should keep the order of words and blank spaces in the sentence.
    // For example:
    // >>> antiShuffle(("Hi"))
    // ("Hi")
    // >>> antiShuffle(("hello"))
    // ("ehllo")
    // >>> antiShuffle(("Hello World!!!"))
    // ("Hello !!!Wdlor")
    public static String antiShuffle(String s) {

        String[] temp = s.split(" ");
        int[] temp1 = new int[temp.length];
        int count=0;
        for(int i=0;i<temp.length;i++){
            char[] ch = temp[i].toCharArray();
            for(int j=0;j<ch.length;j++){
                temp1[count++] = (int)ch[j];
            }
        }
        Arrays.sort(temp1);
        for(int i=0;i<temp1.length;i++){
            temp[i] = ""+temp1[i];
        }
        String output = "";
        for(int i=0;i<temp.length;i++){
            if(i!=temp.length-1){
                output = output+temp[i]+" ";
            }
            else{
                output = output+temp[i];
            }
        }
        return output;
    }
    public static void main(String[] args) {
    assert(antiShuffle(("Hi")).equals(("Hi")));
    assert(antiShuffle(("hello")).equals(("ehllo")));
    assert(antiShuffle(("number")).equals(("bemnru")));
    assert(antiShuffle(("abcd")).equals(("abcd")));
    assert(antiShuffle(("Hello World!!!")).equals(("Hello !!!Wdlor")));
    assert(antiShuffle(("")).equals(("")));
    assert(antiShuffle(("Hi. My name is Mister Robot. How are you?")).equals((".Hi My aemn is Meirst .Rboot How aer ?ouy")));
    }

}
