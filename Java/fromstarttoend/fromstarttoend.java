//Write a program that computes the sum of the integers from start to end, but don’t include the end number
//For example, sumFrom(1, 10) returns 45 since the sum from 1 to 9 is 45.

package fromstarttoend;

import java.util.Scanner;

public class fromstarttoend {
    
    /**
     * @param start
     * @param end
     * @return
     */
    public static int sumFrom(int start,int end){
        int sum = 0;
        for(int x = start; x < end; x++){
            sum = sum + x;
        }
        return(sum);
    }

    /**
     * @param args
     */
    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in); //Create a Scanner object
        System.out.println("Enter your starting number: "); //asking for a number 
        int start = myObj.nextInt(); //Reading user input

        System.out.println("Enter your ending number(non-inclusive): "); 
        //asking for a upper limit
        int end = myObj.nextInt(); //reading user input

        
        System.out.println("Your sum is " + sumFrom(start, end));
    }

}   
