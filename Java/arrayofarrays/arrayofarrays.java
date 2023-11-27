package arrayofarrays;

public class arrayofarrays {
    /**
     * @param args
     */
    public static void main(String[] args) {
        //int matrix [][] = new int[rows] [colums];
        //table[0].length

        int[][] mat = new int[5][10];
        int label = 1;

        for(int r = 0; r < mat.length; r++){
            for(int c = 0; c < mat[r].length; c++){
                mat[r][c] = label;
                label++;
            }
        }

        for(int r = 0; r < mat.length; r++){           //per one outer loop run
            for(int c = 0; c < mat[r].length; c++){    //10 inner loops run
                System.out.print(r); 
                System.out.println(c);
            }
        }

        for(int out = 0; out < 3; out++){
            for(int in = 0; in < 3; in++){
                System.out.print("!");
            }
            System.out.println();
        }

        //printing required picture
        System.out.println("!");
        System.out.println("! !");
        System.out.println("! ! !");

        for(int out = 0; out < 3; out++){
            for(int in = 0; in <= out; in++){
                System.out.print("!");
            }
        }

        for(int out = 0; out < 3; out++){
            for(int in = 0; in <= out; in++){
                System.out.print("!");
            }
        }

    }
}
