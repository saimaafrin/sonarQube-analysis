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

        // This is a classic task for conversion from decimal to binary.
        // The method is called "long division".
        // The idea is to divide the number by 2, and each time you get a remainder you add a "1"
        // to the result string. Each time you get a quotient you move to the next position
        // and repeat the process. The quotient is the number divided by 2, and the remainder is the
        // remainder of the division.
        // The process ends when the quotient is 0.
        // The most important thing to pay attention to is the "division by 2".
        // The binary system uses 2 as its base, so when you divide by 2, each time you get a quotient
        // of 1, and a remainder of 0 or 1.
        // The method works the same way as it does in the real world.
        // Imagine you have 15 apples, and you want to divide them by 2.
        // You give half of them to your friend, and you keep the other half.
        // Now you have 7 apples and you want to divide them by 2 again.
        // You give half of them to your friend, and you keep the other half.
        // And so on...
        // The result is that each time you divide the number by 2, the number of apples you have
        // will decrease by half, and the remainder will be the number of apples you keep.
        // The process ends when the number you have is 0.
        // In this task you need to do the same, but instead of apples you are dividing a number by 2.
        // The result is a string, where each character represents a binary number.
        // The extra "db" characters at the beginning and at the end of the string are there to help
        // with the format.
        // The function should return a string, with each character representing a binary number.
        // Each character in the string will be '0' or '1'.
        // Examples:
        // >>> decimalToBinary((15l))
        // ("db1111db")
        // >>> decimalToBinary((32l))
        // ("db100000db")
        String result = "db";
        while (decimal > 0) {
            // The quotient is the number divided by 2, and the remainder is the remainder of the division.
            long quotient = decimal / 2;
            long remainder = decimal % 2;
            // The next step is to add the remainder to the result string.
            // In the real world this is done by giving the remainder to your friend.
            // Now the number you have is the quotient, and you need to divide it again.
            // And so on...
            // The process ends when the number you have is 0.
            result += Long.toString(remainder);
            // The number is divided by 2.
            decimal = quotient;
        }
        // The result is the string with the binary numbers.
        // The extra "db" characters at the beginning and at the end of the string are there to help
        // with the format.
        // The function should return a string, with each character representing a binary number.
        // Each character in the string will be '0' or '1'.
        // Examples:
        // >>> decimalToBinary((15l))
        // ("db1111db")
        // >>> decimalToBinary((32l))
    }
    public static void main(String[] args) {
    assert(decimalToBinary((0l)).equals(("db0db")));
    assert(decimalToBinary((32l)).equals(("db100000db")));
    assert(decimalToBinary((103l)).equals(("db1100111db")));
    assert(decimalToBinary((15l)).equals(("db1111db")));
    }

}
