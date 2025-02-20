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

        ArrayList<String> result = new ArrayList<String>();
        if (planet1.equals("Sun") || planet2.equals("Sun"))
            return result;
        if (planet1.equals("Earth") || planet2.equals("Earth"))
            result.add("Earth");
        if (planet1.equals("Mars") || planet2.equals("Mars"))
            result.add("Mars");
        if (planet1.equals("Jupiter") || planet2.equals("Jupiter"))
            result.add("Jupiter");
        if (planet1.equals("Saturn") || planet2.equals("Saturn"))
            result.add("Saturn");
        if (planet1.equals("Uranus") || planet2.equals("Uranus"))
            result.add("Uranus");
        if (planet1.equals("Neptune") || planet2.equals("Neptune"))
            result.add("Neptune");
        if (planet1.equals("Venus") || planet2.equals("Venus"))
            result.add("Venus");
        if (planet1.equals("Mars") || planet2.equals("Mars"))
            result.add("Mars");
        if (planet1.equals("Jupiter") || planet2.equals("Jupiter"))
            result.add("Jupiter");
        if (planet1.equals("Saturn") || planet2.equals("Saturn"))
            result.add("Saturn");
        if (planet1.equals("Uranus") || planet2.equals("Uranus"))
            result.add("Uranus");
        if (planet1.equals("Neptune") || planet2.equals("Neptune"))
            result.add("Neptune");
        if (planet1.equals("Venus") || planet2.equals("Venus"))
            result.add("Venus");
        return result;
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
