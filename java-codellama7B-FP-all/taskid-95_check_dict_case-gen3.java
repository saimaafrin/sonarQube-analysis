import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a hash map, return true if all keys are strings in lower 
    // case or all keys are strings in upper case, else return false.
    // The function should return false is the given hash map is empty.
    // Examples:
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", "b", "banana"))))
    // (true)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", "A", "banana", "B", "banana"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("a", "apple", 8l, "banana", "a", "apple"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("Name", "John", "Age", "36", "City", "Houston"))))
    // (false)
    // >>> checkDictCase((new HashMap<String,String>(Map.of("STATE", "NC", "ZIP", "12345"))))
    // (true)
    public static boolean checkDictCase(HashMap<String,String> dict) {

        // Write an solution here
        // 0: lower case
        // 1: upper case
        // 2: mixed case
        // 3: error
        if (dict.size() == 0) return true;
        int caseStatus = 0;
        for (String key : dict.keySet()) {
            if (caseStatus == 0 && Character.isLowerCase(key.charAt(0))) {
                caseStatus = 1;
            } else if (caseStatus == 1 && Character.isUpperCase(key.charAt(0))) {
                caseStatus = 2;
            } else if (caseStatus == 2 && !(Character.isLowerCase(key.charAt(0)) || Character.isUpperCase(key.charAt(0)))) {
                caseStatus = 3;
            }
            if (caseStatus == 3) return false;
        }
        return true;
    }
    public static void main(String[] args) {
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "b", "banana")))) == (true));
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "A", "banana", "B", "banana")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("p", "pineapple", "5", "banana", "a", "apple")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("Name", "John", "Age", "36", "City", "Houston")))) == (false));
    assert(checkDictCase((new HashMap<String,String>(Map.of("STATE", "NC", "ZIP", "12345")))) == (true));
    assert(checkDictCase((new HashMap<String,String>(Map.of("fruit", "Orange", "taste", "Sweet")))) == (true));
    assert(checkDictCase((new HashMap<String,String>())) == (false));
    }

}
