package sumofarray;

public class sumofarray{

public static void main(String[] args) {
    
    int sum = 0;
    int Array1 [] = {12, 34, 56, 76, 89, 42, 0, 2, 30};

    for(int x = 0; x < Array1.length; x++){
        sum = Array1[x] + sum;

    }

    System.out.println(sum);

}
    
}