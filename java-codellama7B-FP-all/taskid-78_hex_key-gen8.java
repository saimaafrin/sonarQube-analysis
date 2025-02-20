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

        long ans = 0;
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == '0') continue;
            if (c == '1') continue;
            if (c == '2') ans += isPrime(2) ? 1 : 0;
            if (c == '3') ans += isPrime(3) ? 1 : 0;
            if (c == '4') continue;
            if (c == '5') ans += isPrime(5) ? 1 : 0;
            if (c == '6') continue;
            if (c == '7') ans += isPrime(7) ? 1 : 0;
            if (c == '8') continue;
            if (c == '9') continue;
            if (c == 'A') ans += isPrime(11) ? 1 : 0;
            if (c == 'B') ans += isPrime(13) ? 1 : 0;
            if (c == 'C') continue;
            if (c == 'D') ans += isPrime(17) ? 1 : 0;
            if (c == 'E') continue;
            if (c == 'F') continue;
        }
        return ans;
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
