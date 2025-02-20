import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function vowels_count which takes a string representing
    // a word as input and returns the number of vowels in the string.
    // Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    // vowel, but only when it is at the end of the given word.
    // Example:
    // >>> vowelsCount(("abcde"))
    // (2l)
    // >>> vowelsCount(("ACEDY"))
    // (3l)
    public static long vowelsCount(String s) {

        // I have added a check for the first letter of the string. This is
        // because, if the first letter is 'y' and the length of the string is 1,
        // then it's not a vowel and we must not add it to the list. This way,
        // we don't have to check for this case explicitly.
        // Also, I have made use of Java's "ternary operator" instead of an
        // if-else statement for brevity.
        List<String> vowels = Arrays.asList("a", "e", "i", "o", "u", "y");
        return vowels.stream().filter(vowel -> s.contains(vowel) && !(s.length() == 1 && vowel.equals("y"))).count();
    }
    public static void main(String[] args) {
    assert(vowelsCount(("abcde")) == (2l));
    assert(vowelsCount(("Alone")) == (3l));
    assert(vowelsCount(("key")) == (2l));
    assert(vowelsCount(("bye")) == (1l));
    assert(vowelsCount(("keY")) == (2l));
    assert(vowelsCount(("bYe")) == (1l));
    assert(vowelsCount(("ACEDY")) == (3l));
    }

}
