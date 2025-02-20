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

        // A helper method that checks if a number is prime.
        boolean isPrime(int n){
            // A helper method that checks if a number is divisible by any other 
            // number.
            boolean isDivisible(int n, int divisor){
                return n % divisor == 0;
            }
            // An if-else statement that checks if a number is divisible by any 
            // other number.
            if(n == 1) return false;
            for(int i = 2; i < n; i++){
                if(isDivisible(n, i)) return false;
            }
            return true;
        }
        // A helper method that gets the number as a long value from a string.
        long asNumber(String str){
            return Long.parseLong(str, 16);
        }
        // A helper method that gets the number as a string from a long value.
        String asString(long n){
            return Long.toHexString(n).toUpperCase();
        }
        // An initial variable that keeps track of the number of the prime 
        // digits.
        long counter = 0;
        // A for-each loop that checks every digit in the hexadecimal string.
        for(String digit: num.split("")){
            // An if-else statement that checks if the current digit is a prime.
            if(isPrime(asNumber(digit))) counter++;
        }
        // The method returns the number of the prime digits.
        return counter;
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
