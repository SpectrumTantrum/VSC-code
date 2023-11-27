package Scoreprogramarraysforloop;

public class scoreforloop {

     /**
     * @param args
     */
    public static void main(String[] args){
        
        int[] scores = {80, 95, 82, 67, 100};
         
        for(int i = 0; i < scores.length; i++){

            System.out.println(scores[i]);

        }

        System.out.println("");

        scores[2] = 72;
        scores[4] = 95;
        
        for(int i = 0; i < scores.length; i++){

            System.out.println(scores[i]);

        }


    }


}
