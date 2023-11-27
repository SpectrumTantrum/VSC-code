package findtargetnumberarray;

public class target91 {
    
    /**
     * @param args
     */
    public static void main(String[] args) {

        int[] scores = {80, 92, 91, 68, 88};
        int index = 0;
        int target = 91;

        for(int counter = 0; counter < scores.length; counter++){

             if (scores[counter] == target){
                System.out.println(counter);
             }
             

         }

    }
    

}
