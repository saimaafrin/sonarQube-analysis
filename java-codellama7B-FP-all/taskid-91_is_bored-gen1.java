import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You'll be given a string of words, and your task is to count the number
    // of boredoms. A boredom is a sentence that starts with the word "I".
    // Sentences are delimited by '.', '?' or '!'.
    // For example:
    // >>> isBored(("Hello world"))
    // (0l)
    // >>> isBored(("The sky is blue. The sun is shining. I love this weather"))
    // (1l)
    public static long isBored(String S) {

        int n = S.length();
        int i = 0;
        int count = 0;
        while (i < n && S.charAt(i) == ' ') ++i;
        if (i == n) return 0L;
        if (S.charAt(i) == '.') return 0L;
        if (S.charAt(i) == '?' || S.charAt(i) == '!') return 1L;
        if (S.charAt(i) == 'I') {
            while (i < n && S.charAt(i) == ' ') ++i;
            while (i < n && S.charAt(i) != ' ' && S.charAt(i) != '.' && S.charAt(i) != '?' && S.charAt(i) != '!') ++i;
            if (S.charAt(i) == '.') return 0L;
            if (S.charAt(i) == '?' || S.charAt(i) == '!') return 1L;
            return 2L;
        }
        return 0L;
    }
    public static void main(String[] args) {
    assert(isBored(("Hello world")) == (0l));
    assert(isBored(("Is the sky blue?")) == (0l));
    assert(isBored(("I love It !")) == (1l));
    assert(isBored(("bIt")) == (0l));
    assert(isBored(("I feel good today. I will be productive. will kill It")) == (2l));
    assert(isBored(("You and I are going for a walk")) == (0l));
    }

}
