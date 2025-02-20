import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // There are eight planets in our solar system: the closerst to the Sun 
    // is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    // Uranus, Neptune.
    // Write a function that takes two planet names as strings planet1 and planet2. 
    // The function should return a pair containing all planets whose orbits are 
    // located between the orbit of planet1 and the orbit of planet2, sorted by 
    // the proximity to the sun. 
    // The function should return an empty pair if planet1 or planet2
    // are not correct planet names. 
    // Examples
    // >>> bf(("Jupiter"), ("Neptune"))
    // (new ArrayList<String>(Arrays.asList((String)"Saturn", (String)"Uranus")))
    // >>> bf(("Earth"), ("Mercury"))
    // (ArrayList<String>("Venus"))
    // >>> bf(("Mercury"), ("Uranus"))
    // (new ArrayList<String>(Arrays.asList((String)"Venus", (String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn")))
    public static ArrayList<String> bf(String planet1, String planet2) {

        var ans = new ArrayList<String>();
        switch (planet1) {
            case "Mercury":
                switch (planet2) {
                    case "Venus":
                        ans.add("Venus");
                    case "Earth":
                        ans.add("Earth");
                    case "Mars":
                        ans.add("Mars");
                    case "Jupiter":
                        ans.add("Jupiter");
                    case "Saturn":
                        ans.add("Saturn");
                }
            break;
            case "Venus":
                switch (planet2) {
                    case "Earth":
                        ans.add("Earth");
                    case "Mars":
                        ans.add("Mars");
                    case "Jupiter":
                        ans.add("Jupiter");
                    case "Saturn":
                        ans.add("Saturn");
                }
            break;
            case "Earth":
                switch (planet2) {
                    case "Mars":
                        ans.add("Mars");
                    case "Jupiter":
                        ans.add("Jupiter");
                    case "Saturn":
                        ans.add("Saturn");
                }
            break;
            case "Mars":
                switch (planet2) {
                    case "Jupiter":
                        ans.add("Jupiter");
                    case "Saturn":
                        ans.add("Saturn");
                }
            break;
            case "Jupiter":
                switch (planet2) {
                    case "Saturn":
                        ans.add("Saturn");
                    case "Uranus":
                        ans.add("Uranus");
                    case "Neptune":
                        ans.add("Neptune");
                }
            break;
            case "Saturn":
                switch (planet2) {
                    case "Uranus":
                        ans.add("Uranus");
                    case "Neptune":
                        ans.add("Neptune");
                }
            break;
            case "Uranus":
                switch (planet2) {
                    case "Neptune":
                        ans.add("Neptune");
                }
            break;
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(bf(("Jupiter"), ("Neptune")).equals((new ArrayList<String>(Arrays.asList((String)"Saturn", (String)"Uranus")))));
    assert(bf(("Earth"), ("Mercury")).equals((new ArrayList<String>(Arrays.asList((String)"Venus")))));
    assert(bf(("Mercury"), ("Uranus")).equals((new ArrayList<String>(Arrays.asList((String)"Venus", (String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn")))));
    assert(bf(("Neptune"), ("Venus")).equals((new ArrayList<String>(Arrays.asList((String)"Earth", (String)"Mars", (String)"Jupiter", (String)"Saturn", (String)"Uranus")))));
    assert(bf(("Earth"), ("Earth")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(bf(("Mars"), ("Earth")).equals((new ArrayList<String>(Arrays.asList()))));
    assert(bf(("Jupiter"), ("Makemake")).equals((new ArrayList<String>(Arrays.asList()))));
    }

}
