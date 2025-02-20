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

        ArrayList<Integer> numberArray = new ArrayList<Integer>();
        for(int i = 0; i < numbers.length(); i++)
        {
            switch (numbers.charAt(i))
            {
                case 'zero':
                    numberArray.add(0);
                    break;
                case 'one':
                    numberArray.add(1);
                    break;
                case 'two':
                    numberArray.add(2);
                    break;
                case 'three':
                    numberArray.add(3);
                    break;
                case 'four':
                    numberArray.add(4);
                    break;
                case 'five':
                    numberArray.add(5);
                    break;
                case 'six':
                    numberArray.add(6);
                    break;
                case 'seven':
                    numberArray.add(7);
                    break;
                case 'eight':
                    numberArray.add(8);
                    break;
                case 'nine':
                    numberArray.add(9);
                    break;
                default:
                    break;
            }
        }
        Collections.sort(numberArray);
        StringBuilder sortedNumbers = new StringBuilder();
        for(int i = 0; i < numberArray.size(); i++)
        {
            switch (numberArray.get(i))
            {
                case 0:
                    sortedNumbers.append("zero ");
                    break;
                case 1:
                    sortedNumbers.append("one ");
                    break;
                case 2:
                    sortedNumbers.append("two ");
                    break;
                case 3:
                    sortedNumbers.append("three ");
                    break;
                case 4:
                    sortedNumbers.append("four ");
                    break;
                case 5:
                    sortedNumbers.append("five ");
                    break;
                case 6:
                    sortedNumbers.append("six ");
                    break;
                case 7:
                    sortedNumbers.append("seven ");
                    break;
                case 8:
                    sortedNumbers.append("eight ");
                    break;
                case 9:
                    sortedNumbers.append("nine ");
                    break;
                default:
                    break;
            }
        }
        return sortedNumbers.toString();
    }
    public static void main(String[] args) {
    assert(sortNumbers(("")).equals(("")));
    assert(sortNumbers(("three")).equals(("three")));
    assert(sortNumbers(("three five nine")).equals(("three five nine")));
    assert(sortNumbers(("five zero four seven nine eight")).equals(("zero four five seven eight nine")));
    assert(sortNumbers(("six five four three two one zero")).equals(("zero one two three four five six")));
    }

}
