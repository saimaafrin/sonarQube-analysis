import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You have been tasked to write a function that receives 
    // a hexadecimal number as a string and counts the number of hexadecimal 
    // digits that are primes (prime number, or a prime, is a natural number 
    // greater than 1 that is not a product of two smaller natural numbers).
    // Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    // Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    // So you have to determine a number of the following digits: 2, 3, 5, 7, 
    // B (=decimal 11), D (=decimal 13).
    // Note: you may assume the input is always correct or empty string, 
    // and symbols A,B,C,D,E,F are always uppercase.
    // Examples:
    // >>> hexKey(("AB"))
    // (1l)
    // >>> hexKey(("1077E"))
    // (2l)
    // >>> hexKey(("ABED1A33"))
    // (4l)
    // >>> hexKey(("123456789ABCDEF0"))
    // (6l)
    // >>> hexKey(("2020"))
    // (2l)
    public static long hexKey(String num) {

        int len = num.length();
        int[] arr = new int[len];
        for(int i = 0; i < len; i++) {
            char c = num.charAt(i);
            if (c == 'A') {
                arr[i] = 10;
            } else if (c == 'B') {
                arr[i] = 11;
            } else if (c == 'C') {
                arr[i] = 12;
            } else if (c == 'D') {
                arr[i] = 13;
            } else if (c == 'E') {
                arr[i] = 14;
            } else if (c == 'F') {
                arr[i] = 15;
            } else {
                arr[i] = Integer.valueOf(String.valueOf(c));
            }
        }
        int count = 0;
        for(int i = 0; i < len; i++) {
            int n = arr[i];
            int k = 0;
            while(n > 0) {
                k = k + 1;
                n = n / 2;
            }
            if (k == 6) {
                count = count + 1;
            }
        }
        return Long.valueOf(String.valueOf(count));
    }
    public static void main(String[] args) {
    assert(hexKey(("AB")) == (1l));
    assert(hexKey(("1077E")) == (2l));
    assert(hexKey(("ABED1A33")) == (4l));
    assert(hexKey(("2020")) == (2l));
    assert(hexKey(("123456789ABCDEF0")) == (6l));
    assert(hexKey(("112233445566778899AABBCCDDEEFF00")) == (12l));
    }

}
