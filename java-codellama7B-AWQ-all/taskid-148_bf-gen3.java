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

      // Write your code here
      if (planet1.equals("Mercury")) {
        planet1 = "Venus";
      } else if (planet1.equals("Earth")) {
        planet1 = "Mars";
      } else if (planet1.equals("Mars")) {
        planet1 = "Jupiter";
      } else if (planet1.equals("Jupiter")) {
        planet1 = "Saturn";
      } else if (planet1.equals("Saturn")) {
        planet1 = "Uranus";
      } else if (planet1.equals("Uranus")) {
        planet1 = "Neptune";
      } else {
        return new ArrayList<String>();
      }
      if (planet2.equals("Mercury")) {
        planet2 = "Venus";
      } else if (planet2.equals("Earth")) {
        planet2 = "Mars";
      } else if (planet2.equals("Mars")) {
        planet2 = "Jupiter";
      } else if (planet2.equals("Jupiter")) {
        planet2 = "Saturn";
      } else if (planet2.equals("Saturn")) {
        planet2 = "Uranus";
      } else if (planet2.equals("Uranus")) {
        planet2 = "Neptune";
      } else {
        return new ArrayList<String>();
      }
      ArrayList<String> planets = new ArrayList<String>();
      planets.add(planet1);
      planets.add(planet2);
      for (int i = 0; i < planets.size() - 1; i++) {
        for (int j = i + 1; j < planets.size(); j++) {
          if (planets.get(j).compareTo(planets.get(i)) < 0) {
            String tmp = planets.get(i);
            planets.set(i, planets.get(j));
            planets.set(j, tmp);
          }
        }
      }
      return planets;
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
