

package Linearsearch;

import  java.util.Scanner;

public class Linearsearch {
    /**
     * @param args
     */
    public static void main(String[] args) {
        int found = -1;
        int[] array = {12, 23, 34, 45, 50, 45, 33, 23,50};
        Scanner kb = new Scanner(System.in);
        System.out.println("Enter any number to search:");
        int choice = kb.nextInt();

        for(int i = 0; i < array.length; i++){
            if (choice == array[i]){
                found = 1;
                break;
            }
        }
        
        if(found == 1){
            System.out.println("The number you are searching for is found in the list");
        }
        else{
            System.out.println("The number you are searching for is not found in the list");
        }
    }
}
