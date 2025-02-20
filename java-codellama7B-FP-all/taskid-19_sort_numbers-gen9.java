import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input is a space-delimited string of numberals from 'zero' to 'nine'.
    // Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    // Return the string with numbers sorted from smallest to largest
    // >>> sortNumbers(("three one five"))
    // ("one three five")
    public static String sortNumbers(String numbers) {

        ArrayList<Integer> numList = new ArrayList<>();
        for (int i = 0; i < numbers.length(); i++) {
            switch (numbers.charAt(i)) {
                case 'zero':
                    numList.add(0);
                    break;
                case 'one':
                    numList.add(1);
                    break;
                case 'two':
                    numList.add(2);
                    break;
                case 'three':
                    numList.add(3);
                    break;
                case 'four':
                    numList.add(4);
                    break;
                case 'five':
                    numList.add(5);
                    break;
                case 'six':
                    numList.add(6);
                    break;
                case 'seven':
                    numList.add(7);
                    break;
                case 'eight':
                    numList.add(8);
                    break;
                case 'nine':
                    numList.add(9);
                    break;
            }
        }
        Collections.sort(numList);
        String result = "";
        for (int num : numList) {
            result += Character.toString(num + '0');
        }
        return result;
    }
    public static void main(String[] args) {
    assert(sortNumbers(("")).equals(("")));
    assert(sortNumbers(("three")).equals(("three")));
    assert(sortNumbers(("three five nine")).equals(("three five nine")));
    assert(sortNumbers(("five zero four seven nine eight")).equals(("zero four five seven eight nine")));
    assert(sortNumbers(("six five four three two one zero")).equals(("zero one two three four five six")));
    }

}
