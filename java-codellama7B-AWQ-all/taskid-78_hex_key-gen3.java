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

        List<String> primeHexNumbers = new ArrayList<>();
        long numberOfPrimeHexNumbers = 0;
        for(int i = 0; i < num.length(); i++) {
            switch(num.charAt(i)) {
                case 'A':
                    primeHexNumbers.add("10");
                    break;
                case 'B':
                    primeHexNumbers.add("11");
                    break;
                case 'C':
                    primeHexNumbers.add("12");
                    break;
                case 'D':
                    primeHexNumbers.add("13");
                    break;
                case 'E':
                    primeHexNumbers.add("14");
                    break;
                case 'F':
                    primeHexNumbers.add("15");
                    break;
                case '0':
                    primeHexNumbers.add("0");
                    break;
                case '1':
                    primeHexNumbers.add("1");
                    break;
                case '2':
                    primeHexNumbers.add("2");
                    break;
                case '3':
                    primeHexNumbers.add("3");
                    break;
                case '4':
                    primeHexNumbers.add("4");
                    break;
                case '5':
                    primeHexNumbers.add("5");
                    break;
                case '6':
                    primeHexNumbers.add("6");
                    break;
                case '7':
                    primeHexNumbers.add("7");
                    break;
                case '8':
                    primeHexNumbers.add("8");
                    break;
                case '9':
                    primeHexNumbers.add("9");
                    break;
            }
        }
        for(int i = 0; i < primeHexNumbers.size(); i++) {
            if(isPrime(Long.parseLong(primeHexNumbers.get(i)))) {
                numberOfPrimeHexNumbers++;
            }
        }
        return numberOfPrimeHexNumbers;
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
