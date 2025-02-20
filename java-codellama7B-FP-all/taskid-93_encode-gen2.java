import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes a message, and encodes in such a 
    // way that it swaps case of all letters, replaces all vowels in 
    // the message with the letter that appears 2 places ahead of that 
    // vowel in the english alphabet. 
    // Assume only letters. 
    // Examples:
    // >>> encode(("test"))
    // ("TGST")
    // >>> encode(("This is a message"))
    // ("tHKS KS C MGSSCGG")
    public static String encode(String message) {

        // your code here
        // 借助暗转明, 明转暗
        StringBuffer sb = new StringBuffer();
        // 字符串转化成char数组
        char[] array = message.toCharArray();
        for(int i = 0; i < array.length; i++){
            if(array[i] >= 65 && array[i] <= 90){
                sb.append((char)(array[i] + 32));
            }else if(array[i] >= 97 && array[i] <= 122){
                sb.append((char)(array[i] - 32));
            }else{
                sb.append(array[i]);
            }
        }
        // 字符串转化成char数组
        array = sb.toString().toCharArray();
        for(int i = 0; i < array.length; i++){
            // 大写字母进行替换
            if(array[i] >= 65 && array[i] <= 90){
                if(array[i] == 90 || array[i] == 122){
                    sb.append((char)65);
                }else{
                    sb.append((char)(array[i] + 2));
                }
            }
            // 小写字母进行替换
            else if(array[i] >= 97 && array[i] <= 122){
                if(array[i] == 122 || array[i] == 90){
                    sb.append((char)97);
                }else{
                    sb.append((char)(array[i] + 2));
                }
            }else{
                sb.append(array[i]);
            }
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    assert(encode(("TEST")).equals(("tgst")));
    assert(encode(("Mudasir")).equals(("mWDCSKR")));
    assert(encode(("YES")).equals(("ygs")));
    assert(encode(("This is a message")).equals(("tHKS KS C MGSSCGG")));
    assert(encode(("I DoNt KnOw WhAt tO WrItE")).equals(("k dQnT kNqW wHcT Tq wRkTg")));
    }

}
