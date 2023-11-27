//Write a method that returns whether a is evenly divisible by b.

package isadevisable;

import java.util.Scanner;

public class isadevisable {

    public static boolean isDivisible(int dividend, int divisor){
        int a = dividend;
        int b = divisor;

        if (a % b == 0){
            return(true);
        }
        else{
            return(false);
        }
    }

    /**
     * @param args
     */
    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in); //Create a Scanner object
        System.out.println("Enter your dividend number: "); //asking for a number 
        int dividend = myObj.nextInt(); //Reading user input

        System.out.println("Enter your divisor number: "); 
        //asking for a upper limit
        int divisor = myObj.nextInt(); //reading user input

        if(isDivisible(dividend, divisor) == true){
            System.out.println("Your number a can be divided by b evenly");
        }
        else{
            System.out.println("Your number a cannot be divided by b evenly");
        }
    }
}
