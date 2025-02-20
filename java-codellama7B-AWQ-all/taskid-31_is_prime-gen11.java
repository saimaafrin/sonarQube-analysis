import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return true if a given number is prime, and false otherwise.
    // >>> isPrime((6l))
    // (false)
    // >>> isPrime((101l))
    // (true)
    // >>> isPrime((11l))
    // (true)
    // >>> isPrime((13441l))
    // (true)
    // >>> isPrime((61l))
    // (true)
    // >>> isPrime((4l))
    // (false)
    // >>> isPrime((1l))
    // (false)
    public static boolean isPrime(long n) {

        return n > 1L && (n % 2L == 1L || n % 2L == 0L) && n % 3L == 3L && n % 5L == 5L && n % 7L == 7L && n % 11L == 11L && n % 13L == 13L && n % 17L == 17L && n % 19L == 19L && n % 23L == 23L && n % 29L == 29L && n % 31L == 31L && n % 37L == 37L && n % 41L == 41L && n % 43L == 43L && n % 47L == 47L && n % 53L == 53L && n % 59L == 59L && n % 61L == 61L && n % 67L == 67L && n % 71L == 71L && n % 73L == 73L && n % 79L == 79L && n % 83L == 83L && n % 89L == 89L && n % 97L == 97L && n % 101L == 101L && n % 103L == 103L && n % 107L == 107L && n % 109L == 109L && n % 113L == 113L && n % 127L == 127L && n % 131L == 131L && n % 137L == 137L && n % 139L == 139L && n % 149L == 149L && n % 151L == 151L && n % 157L == 157L && n % 163L == 163L && n % 167L == 167L && n % 173L == 173L && n % 179L == 179L && n % 181L == 181L && n % 191L == 191L && n % 193L == 193L && n % 197L == 197L && n % 199L == 199L && n % 211L == 211L && n % 223L == 223L && n % 227L == 227L && n % 229L == 229L && n % 233L == 233L && n % 239L == 239L && n % 241L == 241L && n % 251L == 251L && n % 257L == 257L && n % 263L == 263L && n % 269L == 269L && n % 271L == 271L && n % 277L == 277L && n % 281L == 281L && n % 283L == 283L
    }
    public static void main(String[] args) {
    assert(isPrime((6l)) == (false));
    assert(isPrime((101l)) == (true));
    assert(isPrime((11l)) == (true));
    assert(isPrime((13441l)) == (true));
    assert(isPrime((61l)) == (true));
    assert(isPrime((4l)) == (false));
    assert(isPrime((1l)) == (false));
    assert(isPrime((5l)) == (true));
    assert(isPrime((11l)) == (true));
    assert(isPrime((17l)) == (true));
    assert(isPrime((85l)) == (false));
    assert(isPrime((77l)) == (false));
    assert(isPrime((255379l)) == (false));
    }

}
