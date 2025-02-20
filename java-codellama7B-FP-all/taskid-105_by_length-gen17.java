import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list of integers, sort the integers that are between 1 and 9 inclusive,
    // reverse the resulting array array list, and then replace each digit by its corresponding name from
    // "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    // For example:
    // >>> byLength((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)1l, (long)4l, (long)5l, (long)8l, (long)2l, (long)3l))))
    // (new ArrayList<String>(Arrays.asList((String)"Eight", (String)"Five", (String)"Four", (String)"Three", (String)"Two", (String)"Two", (String)"One", (String)"One")))
    // If the array array list is empty, return an empty array array list:
    // >>> byLength((new ArrayList<Long>(Arrays.asList())))
    // (new ArrayList<String>(Arrays.asList()))
    // If the array array list has any strange number ignore it:
    // >>> byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)55l))))
    // (new ArrayList<String>(Arrays.asList((String)"One")))
    public static ArrayList<String> byLength(ArrayList<Long> arr) {

        // This is a "method-only" submission.
        // You only need to complete this method.
        // This method takes an array list of integers and returns an array list of strings.
        // The strings are the corresponding names of the numbers from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
        // The numbers should be sorted from smallest to largest and the resulting array list should be sorted from largest to smallest.
        // Any number outside of the range 1 to 9 should be ignored.
        // If the input array list is empty, an empty array list should be returned.

        Map<Long, String> map = new HashMap<>();
        map.put(1l, "One");
        map.put(2l, "Two");
        map.put(3l, "Three");
        map.put(4l, "Four");
        map.put(5l, "Five");
        map.put(6l, "Six");
        map.put(7l, "Seven");
        map.put(8l, "Eight");
        map.put(9l, "Nine");

        if (arr.isEmpty()) {
            return new ArrayList<>();
        }

        List<Long> betweenOneAndNine = arr.stream()
            .filter(a -> a >= 1l && a <= 9l)
            .sorted()
            .collect(Collectors.toList());

        List<String> betweenOneAndNineNames = new ArrayList<>();
        for (Long num: betweenOneAndNine) {
            betweenOneAndNineNames.add(map.get(num));
        }

        Collections.reverse(betweenOneAndNineNames);

        return new ArrayList<>(betweenOneAndNineNames);
    }
    public static void main(String[] args) {
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)1l, (long)4l, (long)5l, (long)8l, (long)2l, (long)3l)))).equals((new ArrayList<String>(Arrays.asList((String)"Eight", (String)"Five", (String)"Four", (String)"Three", (String)"Two", (String)"Two", (String)"One", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<String>(Arrays.asList()))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)55l)))).equals((new ArrayList<String>(Arrays.asList((String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)3l, (long)2l)))).equals((new ArrayList<String>(Arrays.asList((String)"Three", (String)"Two", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)9l, (long)4l, (long)8l)))).equals((new ArrayList<String>(Arrays.asList((String)"Nine", (String)"Eight", (String)"Four")))));
    }

}
