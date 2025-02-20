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

        ArrayList<String> result = new ArrayList<>();
        if (arr.size() == 0) return result;
        TreeMap<Long, Integer> map = new TreeMap<Long, Integer>();
        for (int i = 0; i < arr.size(); i++) {
            Long l = arr.get(i);
            if (l > 0 && l <= 9) {
                map.put(l, map.getOrDefault(l, 0) + 1);
            }
        }
        ArrayList<Long> ans = new ArrayList<Long>();
        for (Map.Entry<Long, Integer> entry : map.entrySet()) {
            ans.add(entry.getKey());
        }
        ans.sort(Comparator.naturalOrder());
        Collections.reverse(ans);
        for (int i = 0; i < ans.size(); i++) {
            switch (ans.get(i)) {
                case 1L:
                    result.add("One");
                    break;
                case 2L:
                    result.add("Two");
                    break;
                case 3L:
                    result.add("Three");
                    break;
                case 4L:
                    result.add("Four");
                    break;
                case 5L:
                    result.add("Five");
                    break;
                case 6L:
                    result.add("Six");
                    break;
                case 7L:
                    result.add("Seven");
                    break;
                case 8L:
                    result.add("Eight");
                    break;
                case 9L:
                    result.add("Nine");
                    break;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)1l, (long)4l, (long)5l, (long)8l, (long)2l, (long)3l)))).equals((new ArrayList<String>(Arrays.asList((String)"Eight", (String)"Five", (String)"Four", (String)"Three", (String)"Two", (String)"Two", (String)"One", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<String>(Arrays.asList()))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)55l)))).equals((new ArrayList<String>(Arrays.asList((String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)1l, (long)-1l, (long)3l, (long)2l)))).equals((new ArrayList<String>(Arrays.asList((String)"Three", (String)"Two", (String)"One")))));
    assert(byLength((new ArrayList<Long>(Arrays.asList((long)9l, (long)4l, (long)8l)))).equals((new ArrayList<String>(Arrays.asList((String)"Nine", (String)"Eight", (String)"Four")))));
    }

}
