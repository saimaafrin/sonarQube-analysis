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

        ArrayList<String> names = new ArrayList<String>();
        if (arr.size() > 0) {
            // sort numbers between 1 and 9 inclusive
            Long[] sorted = arr.stream().filter(x -> x > 0 && x < 10).sorted().toArray(Long[]::new);
            // reverse the sorted array
            Long[] reversed = Stream.of(sorted).reduce((a, b) -> b).get().longValue() - sorted[0] < 0 ? sorted : reverse(sorted);
            // replace numbers by their names
            for (int i = 0; i < reversed.length; i++) {
                switch ((int) reversed[i]) {
                    case 1:
                        names.add("One");
                        break;
                    case 2:
                        names.add("Two");
                        break;
                    case 3:
                        names.add("Three");
                        break;
                    case 4:
                        names.add("Four");
                        break;
                    case 5:
                        names.add("Five");
                        break;
                    case 6:
                        names.add("Six");
                        break;
                    case 7:
                        names.add("Seven");
                        break;
                    case 8:
                        names.add("Eight");
                        break;
                    case 9:
                        names.add("Nine");
                        break;
                    default:
                        names.add("");
                        break;
                }
            }
        }
        return names;
    }
    public static void main(String[] args) {
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)1l, (long)4l, (long)5l, (long)8l, (long)2l, (long)3l)))).equals((new ArrayList<String>(Arrays.asList((String)"Eight", (String)"Five", (String)"Four", (String)"Three", (String)"Two", (String)"Two", (String)"One", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<String>(Arrays.asList()))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)55l)))).equals((new ArrayList<String>(Arrays.asList((String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)3l, (long)2l)))).equals((new ArrayList<String>(Arrays.asList((String)"Three", (String)"Two", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)9l, (long)4l, (long)8l)))).equals((new ArrayList<String>(Arrays.asList((String)"Nine", (String)"Eight", (String)"Four")))));
    }

}
