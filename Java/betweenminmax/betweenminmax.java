package betweenminmax;

import java.util.Scanner;

//Write a method that takes 3 parameters and returns 
//whether num is between min and max inclusive

//It should return true if num is in between min and max
//,inclusive and return false otherwise

public class betweenminmax{

    /**
* Fill this in with a Javadoc style comment.
*/
    public static boolean inRange(double num, double min, double max){
        if(num >= min && num <= max){
            return(true);
        }
        else{
            return(false);
        }
    }  

    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in); //Create a Scanner object
        System.out.println("Enter your number "); //asking for a number 
        double num = myObj.nextDouble(); //Reading user input

        System.out.println("Enter your maximum number(inclusive): "); 
        //asking for a upper limit
        double max = myObj.nextDouble(); //reading user input

        System.out.println("Enter yout minimum number(inclusive); ");
        //asking for a lower limit
        double min = myObj.nextDouble(); //reading user input
        
        System.out.println("Your number is: " + inRange(num, min, max));
    }
    
}