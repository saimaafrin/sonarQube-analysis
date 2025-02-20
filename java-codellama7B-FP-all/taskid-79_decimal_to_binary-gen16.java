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

        StringBuilder binary = new StringBuilder("db");
        int n = 0;
        long d = 1;
        while (decimal > 0) {
            if (decimal / d == 0) {
                binary.append(0);
            } else if (decimal / d == 1) {
                binary.append(1);
            }
            n++;
            if (n == 8) {
                binary.append("db");
                n = 0;
            }
            d *= 2;
            decimal -= (decimal / d) * d;
        }
        if (n != 0) {
            binary.append("db");
        }
        return binary.reverse().toString();
    }
    public static void main(String[] args) {
    assert(decimalToBinary((0l)).equals(("db0db")));
    assert(decimalToBinary((32l)).equals(("db100000db")));
    assert(decimalToBinary((103l)).equals(("db1100111db")));
    assert(decimalToBinary((15l)).equals(("db1111db")));
    }

}
