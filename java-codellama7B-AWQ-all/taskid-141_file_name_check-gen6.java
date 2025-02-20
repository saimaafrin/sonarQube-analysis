import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Create a function which takes a string representing a file's name, and returns
    // 'Yes' if the the file's name is valid, and returns 'No' otherwise.
    // A file's name is considered to be valid if and only if all the following conditions 
    // are met:
    // - There should not be more than three digits ('0'-'9') in the file's name.
    // - The file's name contains exactly one dot '.'
    // - The substring before the dot should not be empty, and it starts with a letter from 
    // the latin alphapet ('a'-'z' and 'A'-'Z').
    // - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    // Examples:
    // >>> fileNameCheck(("example.txt"))
    // ("Yes")
    // >>> fileNameCheck(("1example.dll"))
    // ("No")
    public static String fileNameCheck(String file_name) {

        int i = 0;
        int j = 0;
        String a = "";
        int dot_counter = 0;
        while (i < file_name.length()) {
            if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                j++;
                i++;
            }
            else if (file_name.charAt(i) == '.') {
                dot_counter++;
                i++;
            }
            else {
                a = a + file_name.charAt(i);
                i++;
            }
        }
        if (j > 3) {
            return "No";
        }
        else if (dot_counter != 1) {
            return "No";
        }
        else if (j == 0 || j == 3) {
            return "No";
        }
        else if (a.length() == 0) {
            return "No";
        }
        else if (a.charAt(0) < 'a' || (a.charAt(0) > 'z' && a.charAt(0) < 'A') || (a.charAt(0) > 'Z')) {
            return "No";
        }
        else if (file_name.charAt(file_name.length() - 4) == 't' && file_name.charAt(file_name.length() - 3) == 'x' && file_name.charAt(file_name.length() - 2) == 't' && file_name.charAt(file_name.length() - 1) == '.') {
            return "Yes";
        }
        else if (file_name.charAt(file_name.length() - 4) == 'e' && file_name.charAt(file_name.length() - 3) == 'x' && file_name.charAt(file_name.length() - 2) == 'e' && file_name.charAt(file_name.length() - 1) == '.') {
            return "Yes";
        }
        else if (file_name.charAt(file_name.length() - 4) == 'l' && file_name.charAt(file_name.length() - 3) == 'l' && file_name.charAt(file_name.length() - 2) == 'd' && file_name.charAt(file_name.length() - 1) == '.') {
            return "Yes";
        }
        else {
            return "No";
        }
    }
    public static void main(String[] args) {
    assert(fileNameCheck(("example.txt")).equals(("Yes")));
    assert(fileNameCheck(("1example.dll")).equals(("No")));
    assert(fileNameCheck(("s1sdf3.asd")).equals(("No")));
    assert(fileNameCheck(("K.dll")).equals(("Yes")));
    assert(fileNameCheck(("MY16FILE3.exe")).equals(("Yes")));
    assert(fileNameCheck(("His12FILE94.exe")).equals(("No")));
    assert(fileNameCheck(("_Y.txt")).equals(("No")));
    assert(fileNameCheck(("?aREYA.exe")).equals(("No")));
    assert(fileNameCheck(("/this_is_valid.dll")).equals(("No")));
    assert(fileNameCheck(("this_is_valid.wow")).equals(("No")));
    assert(fileNameCheck(("this_is_valid.txt")).equals(("Yes")));
    assert(fileNameCheck(("this_is_valid.txtexe")).equals(("No")));
    assert(fileNameCheck(("#this2_i4s_5valid.ten")).equals(("No")));
    assert(fileNameCheck(("@this1_is6_valid.exe")).equals(("No")));
    assert(fileNameCheck(("this_is_12valid.6exe4.txt")).equals(("No")));
    assert(fileNameCheck(("all.exe.txt")).equals(("No")));
    assert(fileNameCheck(("I563_No.exe")).equals(("Yes")));
    assert(fileNameCheck(("Is3youfault.txt")).equals(("Yes")));
    assert(fileNameCheck(("no_one#knows.dll")).equals(("Yes")));
    assert(fileNameCheck(("1I563_Yes3.exe")).equals(("No")));
    assert(fileNameCheck(("I563_Yes3.txtt")).equals(("No")));
    assert(fileNameCheck(("final..txt")).equals(("No")));
    assert(fileNameCheck(("final132")).equals(("No")));
    assert(fileNameCheck(("_f4indsartal132.")).equals(("No")));
    assert(fileNameCheck((".txt")).equals(("No")));
    assert(fileNameCheck(("s.")).equals(("No")));
    }

}
