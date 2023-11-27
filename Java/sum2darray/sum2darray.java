package sum2darray;

public class sum2darray {
     /**
     * @param args
     */
    public static void main(String[] args) {

        int sum = 0;
        int[][] mat = {{8, 5}, {3, 7, 2}};

        for(int out = 0; out < mat.length; out++){
            for(int in = 0; in < mat[out].length; in++){
                sum = mat[out][in] + sum;
            }
        }

        System.out.println(sum);

    }
}
