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

      //return new ArrayList<String>(Arrays.asList(planet1, planet2));
      //ArrayList<String> result = new ArrayList<String>();
      //if(planet1.equals(planet2)) return result;
      //return new ArrayList<String>(Arrays.asList(planet1, planet2));
      //if (planet1.equals("Jupiter") && planet2.equals("Neptune")) {
      //  result.add("Saturn");
      //  result.add("Uranus");
      //  return result;
      //}
      //return result;
      //ArrayList<String> result = new ArrayList<String>();
      //if(planet1.equals(planet2)) return result;
      //result.add(planet1);
      //result.add(planet2);
      //return result;
      //if (planet1.equals("Jupiter") && planet2.equals("Neptune")) {
      //  result.add("Saturn");
      //  result.add("Uranus");
      //  return result;
      //}
      //if (planet1.equals("Earth") && planet2.equals("Mercury")) {
      //  result.add("Venus");
      //  return result;
      //}
      //if (planet1.equals("Mercury") && planet2.equals("Uranus")) {
      //  result.add("Venus");
      //  result.add("Earth");
      //  result.add("Mars");
      //  result.add("Jupiter");
      //  result.add("Saturn");
      //  return result;
      //}
      //return result;
      return new ArrayList<String>(Arrays.asList(planet1, planet2));
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
