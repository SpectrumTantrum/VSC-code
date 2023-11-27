package parameters;

public class parameterdemo {
    
    public static double average(int gr1, int gr2, int gr3){
        return (gr1 + gr2 + gr3) / 3.0;
    }

    public static void main(String[] args) {
        System.out.println(average(85, 97, 76));
    }

}
