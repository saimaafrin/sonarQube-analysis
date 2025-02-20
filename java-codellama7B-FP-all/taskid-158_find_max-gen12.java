import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that accepts an array array list of strings.
    // The array list contains different words. Return the word with maximum number
    // of unique characters. If multiple strings have maximum number of unique
    // characters, return the one which comes first in lexicographical order.
    // >>> findMax((new ArrayList<String>(Arrays.asList((String)"name", (String)"of", (String)"string"))))
    // ("string")
    // >>> findMax((new ArrayList<String>(Arrays.asList((String)"name", (String)"enam", (String)"game"))))
    // ("enam")
    // >>> findMax((new ArrayList<String>(Arrays.asList((String)"aaaaaaa", (String)"bb", (String)"cc"))))
    // ("aaaaaaa")
    public static String findMax(ArrayList<String> words) {

        // Write your code here
        // int[] ch = new int[26];
        // String max = "";
        // int max_len = 0;
        // for (String word : words) {
        //     int[] cnt = new int[26];
        //     for (int i = 0; i < word.length(); i++) {
        //         cnt[word.charAt(i) - 'a'] += 1;
        //     }
        //     int unique = 0;
        //     for (int i = 0; i < 26; i++) {
        //         if (cnt[i] > 0)
        //             unique += 1;
        //     }
        //     if (unique > max_len) {
        //         max_len = unique;
        //         max = word;
        //     }
        // }
        // return max;

        // 1. Create a HashMap with each char and its frequency
        // 2. Return the word with highest frequency
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        String max = "";
        int max_len = 0;
        for (String word : words) {
            // Update frequency
            for (int i = 0; i < word.length(); i++) {
                String char_ = word.charAt(i) + "";
                if (!map.containsKey(char_))
                    map.put(char_, 0);
                map.put(char_, map.get(char_) + 1);
            }
            // Update word with highest frequency
            if (map.size() > max_len) {
                max_len = map.size();
                max = word;
            }
            // Cleanup map
            map.clear();
        }
        return max;
    }
    public static void main(String[] args) {
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"name", (String)"of", (String)"string")))).equals(("string")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"name", (String)"enam", (String)"game")))).equals(("enam")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"aaaaaaa", (String)"bb", (String)"cc")))).equals(("aaaaaaa")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"abc", (String)"cba")))).equals(("abc")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"play", (String)"this", (String)"game", (String)"of", (String)"footbott")))).equals(("footbott")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"we", (String)"are", (String)"gonna", (String)"rock")))).equals(("gonna")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"we", (String)"are", (String)"a", (String)"mad", (String)"nation")))).equals(("nation")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"this", (String)"is", (String)"a", (String)"prrk")))).equals(("this")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"b")))).equals(("b")));
    assert(findMax((new ArrayList<String>(Arrays.asList((String)"play", (String)"play", (String)"play")))).equals(("play")));
    }

}
