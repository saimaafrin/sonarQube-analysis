import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You will be given a number in decimal form and your task is to convert it to
    // binary format. The function should return a string, with each character representing a binary
    // number. Each character in the string will be '0' or '1'.
    // There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    // The extra characters are there to help with the format.
    // Examples:
    // >>> decimalToBinary((15l))
    // ("db1111db")
    // >>> decimalToBinary((32l))
    // ("db100000db")
    public static String decimalToBinary(long decimal) {

        // Use the formula:
        // binary = (decimal & 1) + (decimal >> 1)
        // You can use & for AND and >> for right shift
        // For example, 15 in binary is 1111, so the above formula works as follows:
        // binary = (15 & 1) + (15 >> 1) = 1 + 7 = 8
        // Now we can do binary again by shifting right one more time:
        // binary = (8 & 1) + (8 >> 1) = 0 + 4 = 4
        // So the result is 1111 in binary.
        return "db" + Long.toBinaryString(decimal) + "db";
    }
    public static void main(String[] args) {
    assert(decimalToBinary((0l)).equals(("db0db")));
    assert(decimalToBinary((32l)).equals(("db100000db")));
    assert(decimalToBinary((103l)).equals(("db1100111db")));
    assert(decimalToBinary((15l)).equals(("db1111db")));
    }

}
