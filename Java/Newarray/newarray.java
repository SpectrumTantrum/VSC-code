package Newarray;

public class newarray {
    
    public static void main(String[] args){

        String[] cities = {"Las vegas", "Minsk", "Sao Paulo"};
        int[] temperature = {104, 73, 80};
        double[] precipitation = {4.17, 26.7, 55.0};

        for(int counter = 0; counter < 4 ; counter++){
            System.out.println(cities[counter] + " has an average annual precipitation of " + precipitation[counter]);
            System.out.println(cities[counter] + " has an average annual high temp of " + precipitation[counter]);
        }
        
    }

}
