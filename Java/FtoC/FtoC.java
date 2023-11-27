//Write a method that takes in the temperature in Fahrenheit and returns the temperature in Celsius.
//Hint: remember to cast your variables.
//Hint: remember the conversion from C to F is C = 5/9 * (F - 32)

package FtoC;

import java.util.Scanner;

public class FtoC {
    
    public static double fahrenheitToCelsius(double degrees){
        return ((degrees * 9/5) + 32);
    }

    /**
     * @param args
     */
    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in); //Create a scanner object
        System.out.println("What is the temperature in Fahrenheit? "); //asks for input
        double degrees = myObj.nextDouble();

    System.out.println("The degree is Degree Celsius is " + fahrenheitToCelsius(degrees));

    }
    
}
