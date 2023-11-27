package bigarray;

public class bigarray {
    
/**
     * @param args
     */
    public static void main(String[] args) {

        int[] scores = {23, 6, 47, 35, 2, 14};
        int total = 0;
        int max = 0;

        for(int counter = 0; counter < scores.length; counter++){

             total = total + scores[counter];

         }

         System.out.println(total);

        for(int x = 0; x < scores.length; x++){

            if(scores[x] > max){
                max = scores[x];
            }

        }

        System.out.println(max);

        for(int x = 0; x < scores.length; x++){

            if(scores[x] % 2 == 0){
                
            }
            else{
                System.out.println(scores[x]);
            }

        }
        

    }

}
