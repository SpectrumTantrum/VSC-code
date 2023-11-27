package ascendingarray;

public class ascendingarray{

/**
 * @param args
 */
public static void main(String[] args) {
    
    int Array1 [] = {12, 34, 56, 76, 89, 42, 0, 2, 30};
    int[] Array2 = new int[9];

    //let x be a counter
    for(int primary = 0; primary < Array1.length; primary++){

        for(int second = primary; second < Array1.length; second++){
            if(Array1[primary] > Array1[second]){
                Array2[primary] = Array1[second];
            
        }


        }



}

for(int i = 0; i < Array2.length; i++){
    System.out.println(Array2[i]);
}

}
}